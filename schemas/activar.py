from pydantic import BaseModel, constr
from typing import Optional

class ActivarRequest(BaseModel):
    ip: constr(strip_whitespace=True)
    bus_id: constr(strip_whitespace=True)
    user_agent: Optional[str] = None  # Info del navegador
    metodo: str  # Ej: "ticket", "comprobante", "publicidad"

class ActivarResponse(BaseModel):
    estado: str  # "exitoso", "rechazado"
    mensaje: str
    expiracion: Optional[str] = None  # si aplica expiración (en tickets)
