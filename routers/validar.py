from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.validar import Validar
from schemas.validar_schema import ValidarCreate, ValidarOut
from database import get_db
from utils.token_utils import verificar_token_rol  # Protección JWT
from datetime import datetime
import traceback
import logging

from schemas.pago_manual import PagoManualIn
from schemas.codigo_manual import CodigoManualIn
from models.pago_manual import PagoManual
from models.codigo_manual import CodigoChofer
from models.ticket import Ticket  # Nuevo registro para trazabilidad

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/validar", response_model=ValidarOut, tags=["Validar"])
def validar_codigo(
    data: ValidarCreate,
    db: Session = Depends(get_db),
    usuario: dict = Depends(verificar_token_rol)
):
    """
    Registra la validación de un código para un usuario en una fecha específica.
    Protegido por JWT (admin o chofer). Evita duplicados por código/usuario/fecha.
    """
    rol = usuario["rol"]
    usuario_id_token = usuario["usuario"]

    if rol != "admin" and data.usuario_id != usuario_id_token:
        raise HTTPException(status_code=403, detail="🚫 No puedes validar código para otro usuario.")

    existe = db.query(Validar).filter(
        Validar.codigo == data.codigo,
        Validar.usuario_id == data.usuario_id,
        Validar.fecha == data.fecha
    ).first()

    if existe:
        raise HTTPException(status_code=400, detail="Ya se validó ese código para ese usuario en esa fecha.")

    fecha_final = data.fecha or datetime.utcnow()

    nuevo_validar = Validar(
        codigo=data.codigo,
        usuario_id=data.usuario_id,
        fecha=fecha_final
    )

    try:
        db.add(nuevo_validar)
        db.commit()
        db.refresh(nuevo_validar)

        # Registrar ticket institucional para trazabilidad
        ticket = Ticket(
            usuario_id=data.usuario_id,
            codigo=data.codigo,
            metodo="codigo_usuario",
            estado="validado",
            fecha=datetime.utcnow()
        )
        db.add(ticket)
        db.commit()

        return nuevo_validar

    except Exception as e:
        db.rollback()
        logger.error(f"Error al registrar código: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="❌ Error interno al registrar validación")


@router.post("/validar-pago", tags=["Validar"])
def validar_pago(data: PagoManualIn, db: Session = Depends(get_db)):
    """
    Registra intento de validación por pago móvil (manual).
    Crea un ticket institucional en estado pendiente.
    """
    intento = PagoManual(
        telefono=data.telefono,
        banco=data.banco,
        referencia=data.referencia,
        monto=data.monto,
        unidad=data.unidad,
        metodo="pago_movil",
        estado="pendiente",
        fecha=datetime.utcnow()
    )
    db.add(intento)

    # Registro institucional del ticket para trazabilidad
    ticket = Ticket(
        usuario_id=None,
        codigo=data.referencia,
        metodo="pago_movil",
        estado="pendiente",
        fecha=datetime.utcnow()
    )
    db.add(ticket)

    db.commit()
    db.refresh(intento)
    return {"estado": "pendiente"}


@router.post("/validar-codigo", tags=["Validar"])
def validar_codigo_manual(data: CodigoManualIn, db: Session = Depends(get_db)):
    """
    Verifica si el código entregado por chofer está activo.
    Devuelve info clave para frontend, registra ticket institucional.
    """
    codigo = db.query(CodigoChofer).filter_by(
        codigo=data.codigo, estado="activo"
    ).first()

    if not codigo:
        raise HTTPException(status_code=400, detail="Código no válido o usado.")

    # Marcar como usado
    codigo.estado = "usado"
    db.commit()

    # Registrar ticket institucional
    ticket = Ticket(
        usuario_id=None,
        codigo=data.codigo,
        metodo="codigo_chofer",
        estado="aprobado",
        fecha=datetime.utcnow(),
        unidad=codigo.unidad,
        chofer=codigo.chofer_id
    )
    db.add(ticket)
    db.commit()

    # Retorno completo para frontend
    return {
        "estado": "aprobado",
        "duracion": codigo.duracion,
        "chofer": codigo.chofer_id,
        "unidad": codigo.unidad,
        "compania": codigo.compania
    }
