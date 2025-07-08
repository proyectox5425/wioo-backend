from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.validar import Validar
from schemas.validar_schema import ValidarCreate, ValidarOut
from database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/validar", response_model=ValidarOut)
def validar_codigo(data: ValidarCreate, db: Session = Depends(get_db)):
    # 🔐 Validación: evitar duplicados por código y usuario en la misma fecha
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

    # 📅 Timestamp automático si no se envía
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
        raise HTTPException(
            status_code=500,
            detail=f"Error al registrar validación: {str(e)}"
        )
