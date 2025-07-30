from sqlalchemy import Column, String, Float, DateTime
from database import Base
from datetime import datetime

class PagoManual(Base):
    __tablename__ = "pago_manual"

    referencia = Column(String, primary_key=True, index=True)
    telefono = Column(String)
    banco = Column(String)
    monto = Column(Float)
    unidad = Column(String)
    metodo = Column(String)
    estado = Column(String, default="pendiente")
    fecha_hora = Column(DateTime, default=datetime.utcnow)
    hash_dispositivo = Column(String)
