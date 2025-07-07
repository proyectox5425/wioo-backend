from pydantic import BaseModel
from typing import Literal, Optional

class RedireccionRespuesta(BaseModel):
    estado: Literal["aprobado", "rechazado", "pendiente"]
    mensaje: Optional[str] = None
    metodo: Optional[str] = None  # "ticket", "comprobante", etc.
    ip_pasajero: Optional[str] = None
