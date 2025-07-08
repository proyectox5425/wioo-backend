from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Comprobante(Base):
    __tablename__ = "comprobantes"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), index=True)  # ✅ Index para búsquedas por usuario
    ticket_id = Column(Integer, ForeignKey("tickets.id"), index=True)    # ✅ Index para trazabilidad por ticket
    fecha = Column(DateTime, default=datetime.utcnow, index=True)        # ✅ UTC + index para orden cronológico
    estado = Column(String, index=True)  # ✅ Index para filtrar por estado ('pendiente', 'validado', etc.)

    usuario = relationship("Usuario", back_populates="comprobantes")
    ticket = relationship("Ticket", back_populates="comprobantes")

    def __repr__(self):
        return f"<Comprobante usuario_id={self.usuario_id} ticket_id={self.ticket_id} estado={self.estado}>"
