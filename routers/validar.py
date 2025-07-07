from fastapi import APIRouter, Request
from schemas.dispositivo import Dispositivo
from services.validar import validar_ip
from core.security import verificar_token  # 👈 Protección agregada

router = APIRouter()

@router.post("/validar")
def validar_acceso(data: Dispositivo, request: Request):
    verificar_token(request)  # 🔐 Validación obligatoria del token
    return validar_ip(data.ip)
