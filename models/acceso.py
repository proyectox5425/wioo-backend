from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Acceso(Base):
    __tablename__ = "accesos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), index=True)  # ✅ Index para búsquedas por usuario
    fecha = Column(DateTime, default=datetime.utcnow, index=True)        # ✅ UTC + index para orden cronológico
    ip = Column(String, index=True)                                      # ✅ Index para trazabilidad por IP
    tipo = Column(String)

    usuario = relationship("Usuario", back_populates="accesos")

    def __repr__(self):
        return f"<Acceso usuario_id={self.usuario_id} ip={self.ip} tipo={self.tipo}>"
