from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from models.redireccionar import Redireccionar
from schemas.redireccionar_schema import RedireccionCreate, RedireccionOut
from database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/redireccionar", response_model=RedireccionOut)
def registrar_redireccion(request: Request, data: RedireccionCreate, db: Session = Depends(get_db)):
    ip_cliente = request.client.host

    # 🔐 Validación: evitar duplicados por IP, URL y usuario en la misma fecha
    existe = db.query(Redireccionar).filter(
        Redireccionar.ip == ip_cliente,
        Redireccionar.url == data.url,
        Redireccionar.fecha == data.fecha,
        Redireccionar.usuario_id == data.usuario_id
    ).first()

    if existe:
        raise HTTPException(
            status_code=400,
            detail="Ya existe una redirección registrada con esos datos."
        )

    # 📅 Timestamp automático si no se envía
    fecha_final = data.fecha or datetime.utcnow()

    nueva_redireccion = Redireccionar(
        ip=ip_cliente,
        url=data.url,
        fecha=fecha_final,
        usuario_id=data.usuario_id
    )

    try:
        db.add(nueva_redireccion)
        db.commit()
        db.refresh(nueva_redireccion)
        return nueva_redireccion
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error al registrar redirección: {str(e)}"
    )
