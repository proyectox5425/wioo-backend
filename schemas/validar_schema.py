from pydantic import BaseModel, constr
from typing import Literal, Optional
from datetime import datetime

class ValidarPagoRequest(BaseModel):
    referencia: constr(strip_whitespace=True)
    monto: float
    telefono: constr(strip_whitespace=True)
    tipo: Literal["pago_movil", "transferencia"]
    banco_emisor: Optional[str] = None
    banco_receptor: Optional[str] = None
    fecha: Optional[datetime] = None
    ip_pasajero: Optional[str] = None

class ValidarPagoResponse(BaseModel):
    estado: Literal["validado", "rechazado", "pendiente"]
    mensaje: Optional[str] = None
    acceso_autorizado: bool
