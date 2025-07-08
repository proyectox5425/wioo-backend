from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime


class DispositivoBase(BaseModel):
    nombre: constr(min_length=2)  # ✅ Valida longitud mínima del nombre
    tipo: constr(min_length=3)    # ✅ Valida tipo de dispositivo (ej: sensor, router, etc.)
    activo: bool
    usuario_id: int


class DispositivoCreate(DispositivoBase):
    pass  # ✅ Entrada directa heredada


class DispositivoOut(DispositivoBase):
    id: int
    fecha_creacion: Optional[datetime] = None  # ✅ Si tienes timestamp en el modelo

    class Config:
        orm_mode = True  # ✅ Permite compatibilidad con SQLAlchemy


class DispositivoUpdate(BaseModel):
    nombre: Optional[constr(min_length=2)] = None
    tipo: Optional[constr(min_length=3)] = None
    activo: Optional[bool] = None
    usuario_id: Optional[int] = None
