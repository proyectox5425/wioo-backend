from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime

class GenerarTicketRequest(BaseModel):
    bus_id: constr(strip_whitespace=True)
    valor: float  # monto pagado en efectivo

class TicketResponse(BaseModel):
    codigo: str
    creado_en: datetime
    expiracion: datetime
    estado: str  # "pendiente", "usado", "expirado"

class ValidarTicketRequest(BaseModel):
    codigo: constr(strip_whitespace=True)
    ip_pasajero: Optional[str] = None

class ValidarTicketResponse(BaseModel):
    estado: str  # "válido", "inválido", "expirado", "usado"
    mensaje: Optional[str] = None
    acceso_autorizado: bool
