from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from models.mi_ip import MiIP
from schemas.esquema_ip import IPCreate, IPOut
from database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/mi-ip", response_model=IPOut)
def registrar_ip(request: Request, data: IPCreate, db: Session = Depends(get_db)):
    ip_cliente = request.client.host

    # 🔐 Validación: evitar duplicados por IP y fecha
    existe = db.query(MiIP).filter(
        MiIP.ip == ip_cliente,
        MiIP.fecha == data.fecha,
        MiIP.usuario_id == data.usuario_id
    ).first()

    if existe:
        raise HTTPException(
            status_code=400,
            detail="Ya se registró esta IP para ese usuario en esa fecha."
        )

    # 📅 Timestamp automático si no se envía
    fecha_final = data.fecha or datetime.utcnow()

    nueva_ip = MiIP(
        ip=ip_cliente,
        fecha=fecha_final,
        usuario_id=data.usuario_id
    )

    try:
        db.add(nueva_ip)
        db.commit()
        db.refresh(nueva_ip)
        return nueva_ip
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error al registrar IP: {str(e)}"
        )
