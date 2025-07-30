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
    cedula: str         # ✅ Nueva: enviada desde pantalla 3.1
    tiempo: str         # ✅ Nueva: enviada desde pantalla 3.1

class PagoManualOut(BaseModel):
    estado: str
    fecha: datetime
