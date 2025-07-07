from datetime import datetime
from pydantic import BaseModel

class Ticket(BaseModel):
    codigo: str
    bus_id: str
    creado_en: datetime
    expiracion: datetime
    estado: str  # "pendiente", "usado", "expirado"
    ip_pasajero: str = None
    valor: float = 0.0
