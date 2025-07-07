from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    identificador: str  # ej. código de login
    tipo: str            # "chofer" o "admin"
    activo: bool = True
