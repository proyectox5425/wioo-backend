from pydantic import BaseModel, constr
from typing import Optional

class IPRequest(BaseModel):
    ip: constr(strip_whitespace=True)
    bus_id: Optional[str] = None
    user_agent: Optional[str] = None

class IPResponse(BaseModel):
    ip: str
    estado: str  # "registrado", "rechazado", "duplicado"
    mensaje: Optional[str] = None
