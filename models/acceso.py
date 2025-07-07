from datetime import datetime
from pydantic import BaseModel

class Acceso(BaseModel):
    ip: str
    user_agent: str
    timestamp: datetime
    bus_id: str
