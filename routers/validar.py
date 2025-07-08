from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.validar import Validar
from schemas.validar_schema import ValidarCreate, ValidarOut
from database import get_db
from utils.token_utils import verificar_token_rol  # Protección JWT
from datetime import datetime
import traceback
import logging

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
    Evita duplicados por código/usuario/fecha.
    Protegido por JWT (admin o chofer).
    """
    rol = usuario["rol"]
    usuario_id_token = usuario["usuario"]

    # (Opcional) Solo permitir que validen su propio código si no son admin
    if rol != "admin" and data.usuario_id != usuario_id_token:
        raise HTTPException(status_code=403, detail="🚫 No puedes validar código para otro usuario.")

    existe = db.query(Validar).filter(
        Validar.codigo == data.codigo,
        Validar.usuario_id == data.usuario_id,
        Validar.fecha == data.fecha
    ).first()

    if existe:
        raise HTTPException(
            status_code=400,
            detail="Ya se validó ese código para ese usuario en esa fecha."
        )

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
        return nuevo_validar

    except Exception as e:
        db.rollback()
        logger.error(f"Error al registrar código: {traceback.format_exc()}")
        raise HTTPException(
            status_code=500,
            detail="❌ Error interno al registrar validación"
)
