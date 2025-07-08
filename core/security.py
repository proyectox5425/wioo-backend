from datetime import datetime, timedelta
from jose import JWTError, jwt
from core.config import settings
from fastapi import Depends, HTTPException
from typing import Dict, Union


def crear_token(data: Dict[str, Union[str, int]]) -> str:
    """
    Genera un token JWT con datos personalizados y duración definida en .env
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXP_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm="HS256")
    return encoded_jwt


def verificar_token(token: str) -> Dict[str, Union[str, int]]:
    """
    Verifica si el token es válido y no ha expirado.
    Devuelve el payload si está todo bien.
    Lanza ValueError si el token no sirve.
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        exp = payload.get("exp")

        if exp is None or datetime.utcnow() > datetime.utcfromtimestamp(exp):
            raise JWTError("Token expirado")

        return payload
    except JWTError as e:
        raise ValueError(f"Token inválido: {str(e)}")


def verificar_token_admin(token: str = Depends()) -> Dict:
    """
    Verifica que el token sea válido y que el rol sea 'admin'
    """
    datos = verificar_token(token)
    if datos.get("rol") != "admin":
        raise HTTPException(status_code=403, detail="Acceso restringido para administradores")
    return datos


def verificar_token_chofer(token: str = Depends()) -> Dict:
    """
    Verifica que el token sea válido y que el rol sea 'chofer'
    """
    datos = verificar_token(token)
    if datos.get("rol") != "chofer":
        raise HTTPException(status_code=403, detail="Acceso restringido para choferes")
    return datos


def verificar_token_usuario(token: str = Depends()) -> Dict:
    """
    Verifica que el token sea válido y que el rol sea 'usuario'
    """
    datos = verificar_token(token)
    if datos.get("rol") != "usuario":
        raise HTTPException(status_code=403, detail="Acceso restringido para usuarios")
    return datos


def verificar_token_panel(token: str = Depends()) -> Dict:
    """
    Verifica que el token sea válido y que el rol sea 'panel'
    """
    datos = verificar_token(token)
    if datos.get("rol") != "panel":
        raise HTTPException(status_code=403, detail="Acceso restringido para panel")
    return datos


def verificar_token_servicios(token: str = Depends()) -> Dict:
    """
    Verifica que el token sea válido y que el rol sea 'servicios'
    """
    datos = verificar_token(token)
    if datos.get("rol") != "servicios":
        raise HTTPException(status_code=403, detail="Acceso restringido para servicios")
    return datos
