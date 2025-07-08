from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime


class ValidarBase(BaseModel):
    codigo: constr(min_length=4)  # ✅ Valida longitud mínima
    usuario_id: int
    fecha: datetime


class ValidarCreate(ValidarBase):
    pass


class ValidarOut(ValidarBase):
    id: int

    class Config:
        orm_mode = True


class ValidarUpdate(BaseModel):
    codigo: Optional[constr(min_length=4)] = None
    usuario_id: Optional[int] = None
    fecha: Optional[datetime] = None
