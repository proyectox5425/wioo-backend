import jwt
from fastapi import Request, HTTPException
from datetime import datetime, timedelta
from config import settings  # 👈 Cargamos la configuración central

# Algoritmo de firma para el token
JWT_ALGORITHM = "HS256"

def crear_token(usuario: str, rol: str) -> str:
    """
    Genera un token JWT firmado con expiración.

    Args:
        usuario (str): Nombre o ID del usuario
        rol (str): Rol asignado ('admin', 'chofer', etc.)

    Returns:
        str: Token JWT firmado
    """
    payload = {
        "sub": usuario,
        "rol": rol,
        "exp": datetime.utcnow() + timedelta(minutes=settings.JWT_EXP_MIN)
    }

    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def verificar_token(request: Request) -> dict:
    """
    Verifica que el token JWT sea válido y no vencido.

    Args:
        request (Request): Solicitud HTTP de FastAPI

    Returns:
        dict: Payload del token si es válido
    """
    token = request.headers.get("Authorization")

    if not token:
        raise HTTPException(status_code=401, detail="⛔ Token no proporcionado")

    # Si el token viene con 'Bearer ', lo limpiamos
    if token.startswith("Bearer "):
        token = token.replace("Bearer ", "").strip()

    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload  # Contiene 'sub', 'rol', 'exp'
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="⛔ Token vencido")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="⛔ Token inválido")
