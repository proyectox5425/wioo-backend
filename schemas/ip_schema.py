from pydantic import BaseModel, IPvAnyAddress
from typing import Optional
from datetime import datetime


class IPBase(BaseModel):
    ip: IPvAnyAddress  # ✅ Valida IP automáticamente
    fecha: datetime
    usuario_id: int


class IPCreate(IPBase):
    pass


class IPOut(IPBase):
    id: int

    class Config:
        orm_mode = True


class IPUpdate(BaseModel):
    ip: Optional[IPvAnyAddress] = None
    fecha: Optional[datetime] = None
    usuario_id: Optional[int] = None
