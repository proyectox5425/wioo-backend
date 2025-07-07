from fastapi import APIRouter, Request
from core.security import verificar_token

router = APIRouter()

@router.get("/mi-ip", tags=["Herramientas"])
async def obtener_ip(request: Request):
    verificar_token(request)
    ip_cliente = request.client.host
    return {"ip": ip_cliente}
