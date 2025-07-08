from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.activar import Activar
from schemas.activar_schema import ActivarCreate, ActivarOut
from database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/activar", response_model=ActivarOut)
def activar_entidad(data: ActivarCreate, db: Session = Depends(get_db)):
    # 🔐 Validación: evitar duplicados por usuario y fecha
    existe = db.query(Activar).filter(
        Activar.usuario_id == data.usuario_id,
        Activar.fecha == data.fecha
    ).first()

    if existe:
        raise HTTPException(
            status_code=400,
            detail="Ya existe una activación registrada para ese usuario en esa fecha."
        )

    # 📅 Timestamp automático si no se envía
    fecha_final = data.fecha or datetime.utcnow()

    nueva_activacion = Activar(
        activo=data.activo,
        usuario_id=data.usuario_id,
        fecha=fecha_final
    )

    try:
        db.add(nueva_activacion)
        db.commit()
        db.refresh(nueva_activacion)
        return nueva_activacion
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error al registrar activación: {str(e)}"
        )
