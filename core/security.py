from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

# 🔑 Aquí podrías cargar esto desde tu settings.py si gustas
TOKEN_VALIDO = "miclavesecreta123"

def verificar_token(request: Request) -> None:
    token = request.headers.get("Authorization")

    if not token:
        raise HTTPException(status_code=401, detail="⛔ Token no proporcionado")

    # Si usas esquema tipo "Bearer <token>", descomenta esta línea:
    # token = token.replace("Bearer ", "").strip()

    if token != TOKEN_VALIDO:
        raise HTTPException(status_code=401, detail="⛔ Token inválido")
