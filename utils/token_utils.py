from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional, Dict
from config import settings  # Asegúrate de tener settings.JWT_SECRET y JWT_EXP_MINUTES

ALGORITHM = "HS256"

def crear_token(data: dict) -> str:
    to_encode = data.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=settings.JWT_EXP_MINUTES)
    to_encode.update({"exp": expiracion})
    token = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=ALGORITHM)
    return token

def verificar_token(token: str) -> Optional[Dict]:
    try:
        decoded = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        return decoded
    except JWTError:
        return None
