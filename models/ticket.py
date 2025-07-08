from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)  # ✅ Evita duplicados y mejora búsquedas
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), index=True)  # ✅ Index para consultas rápidas
    fecha_creacion = Column(DateTime, default=datetime.utcnow)  # ✅ UTC para entornos distribuidos
    duracion = Column(Integer)

    usuario = relationship("Usuario", back_populates="tickets")

    def __repr__(self):
        return f"<Ticket codigo={self.codigo} usuario_id={self.usuario_id}>"
