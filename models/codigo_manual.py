from sqlalchemy import Column, String, Integer
from database import Base

class CodigoChofer(Base):
    __tablename__ = "codigo_manual"

    codigo = Column(String, primary_key=True, index=True)
    unidad = Column(String)
    duracion = Column(Integer)  # duración en minutos
    estado = Column(String, default="activo")  # puede ser "activo" o "usado"
