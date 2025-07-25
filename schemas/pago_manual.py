from pydantic import BaseModel
from datetime import datetime

class PagoManualIn(BaseModel):
    telefono: str
    banco: str
    referencia: str
    monto: float
    unidad: str

class PagoManualOut(BaseModel):
    estado: str
    fecha: datetime
