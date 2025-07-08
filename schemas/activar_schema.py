from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ActivarBase(BaseModel):
    activo: bool
    usuario_id: int
    fecha: datetime  # ✅ Asegura formato correcto


class ActivarCreate(ActivarBase):
    pass


class ActivarOut(ActivarBase):
    id: int

    class Config:
        orm_mode = True


class ActivarUpdate(BaseModel):
    activo: Optional[bool] = None
    usuario_id: Optional[int] = None
    fecha: Optional[datetime] = None
