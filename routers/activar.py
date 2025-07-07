from fastapi import APIRouter, Request
from schemas.dispositivo import Dispositivo
from services.activar import activar_ip
from core.security import verificar_token  # 👈 Protección

router = APIRouter()

@router.post("/activar")
def activar_acceso(data: Dispositivo, request: Request):
    verificar_token(request)  # 👈 Verificación de token
    return activar_ip(data.ip)
