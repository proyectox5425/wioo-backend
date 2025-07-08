from pydantic import BaseModel, IPvAnyAddress, HttpUrl
from typing import Optional
from datetime import datetime


class RedireccionBase(BaseModel):
    ip: IPvAnyAddress  # ✅ Valida IP automáticamente
    url: HttpUrl       # ✅ Valida formato de URL
    fecha: datetime
    usuario_id: int


class RedireccionCreate(RedireccionBase):
    pass


class RedireccionOut(RedireccionBase):
    id: int

    class Config:
        orm_mode = True


class RedireccionUpdate(BaseModel):
    ip: Optional[IPvAnyAddress] = None
    url: Optional[HttpUrl] = None
    fecha: Optional[datetime] = None
    usuario_id: Optional[int] = None
