from pydantic import BaseModel
from datetime import datetime

class PagoManualIn(BaseModel):
    telefono: str
    banco: str
    referencia: str
    monto: float
    unidad: str
    metodo: str
    estado: str
    hash_dispositivo: str
    fecha_hora: datetime

class PagoManualOut(BaseModel):
    estado: str
    fecha: datetime
