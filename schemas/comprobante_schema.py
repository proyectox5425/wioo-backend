from pydantic import BaseModel, constr
from typing import Literal, Optional
from datetime import datetime

class ComprobanteRequest(BaseModel):
    referencia: constr(strip_whitespace=True)
    telefono: constr(strip_whitespace=True)
    cuenta: constr(strip_whitespace=True)
    monto: float
    tipo: Literal["transferencia", "pago_movil"]
    fecha: Optional[datetime] = None  # Si quieres registrar la fecha explícita

class ComprobanteResponse(BaseModel):
    estado: Literal["pendiente", "validado", "rechazado"]
    mensaje: str
    ip_pasajero: Optional[str] = None
