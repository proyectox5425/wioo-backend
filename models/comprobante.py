from datetime import datetime
from pydantic import BaseModel

class Comprobante(BaseModel):
    referencia: str
    banco_emisor: str
    banco_receptor: str
    monto: float
    fecha: datetime
    tipo: str  # "pago_movil" o "transferencia"
    ip_pasajero: str
    estado: str = "pendiente"  # "pendiente", "validado", "rechazado"
