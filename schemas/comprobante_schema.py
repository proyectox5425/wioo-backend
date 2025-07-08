from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class ComprobanteBase(BaseModel):
    estado: Literal["pendiente", "validado", "rechazado"]  # ✅ Valida estado permitido
    fecha: datetime  # ✅ Asegura formato correcto
    usuario_id: int
    ticket_id: int


class ComprobanteCreate(ComprobanteBase):
    pass  # ✅ Entrada directa heredada del base


class ComprobanteOut(ComprobanteBase):
    id: int

    class Config:
        orm_mode = True  # ✅ Compatibilidad con modelos SQLAlchemy


class ComprobanteUpdate(BaseModel):
    estado: Optional[Literal["pendiente", "validado", "rechazado"]] = None
    fecha: Optional[datetime] = None
    usuario_id: Optional[int] = None
    ticket_id: Optional[int] = None
