from pydantic import BaseModel, constr
from typing import Literal

class UsuarioLoginRequest(BaseModel):
    identificador: constr(strip_whitespace=True)
    clave: constr(strip_whitespace=True)

class UsuarioLoginResponse(BaseModel):
    tipo: Literal["chofer", "admin"]
    token_acceso: str
    nombre: str
    activo: bool
