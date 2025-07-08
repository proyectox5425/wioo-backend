from pydantic import BaseModel, EmailStr, constr
from typing import Optional


class UsuarioBase(BaseModel):
    correo: EmailStr  # ✅ Valida formato de correo automáticamente
    rol: str
    activo: bool

class UsuarioCreate(UsuarioBase):
    contrasena: constr(min_length=6)  # ✅ Valida longitud mínima de contraseña

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True  # ✅ Compatibilidad con modelos SQLAlchemy

class UsuarioLogin(BaseModel):
    correo: EmailStr
    contrasena: str

class UsuarioUpdate(BaseModel):
    correo: Optional[EmailStr] = None
    contrasena: Optional[constr(min_length=6)] = None
    rol: Optional[str] = None
    activo: Optional[bool] = None
