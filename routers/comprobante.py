from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.comprobante import Comprobante
from schemas.comprobante_schema import ComprobanteCreate, ComprobanteOut
from database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/comprobante", response_model=ComprobanteOut)
def crear_comprobante(data: ComprobanteCreate, db: Session = Depends(get_db)):
    # 🔐 Validación: evitar duplicados por ticket y usuario
    existe = db.query(Comprobante).filter(
        Comprobante.ticket_id == data.ticket_id,
        Comprobante.usuario_id == data.usuario_id
    ).first()

    if existe:
        raise HTTPException(
            status_code=400,
            detail="Ya existe un comprobante para ese ticket y usuario."
        )

    # 📅 Timestamp automático si no se envía
    fecha_final = data.fecha or datetime.utcnow()

    nuevo_comprobante = Comprobante(
        estado=data.estado,
        fecha=fecha_final,
        usuario_id=data.usuario_id,
        ticket_id=data.ticket_id
    )

    try:
        db.add(nuevo_comprobante)
        db.commit()
        db.refresh(nuevo_comprobante)
        return nuevo_comprobante
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error al registrar comprobante: {str(e)}"
        )
