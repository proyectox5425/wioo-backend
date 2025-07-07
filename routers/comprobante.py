from fastapi import APIRouter, Request
from core.security import verificar_token
from schemas.comprobante import Comprobante
from services.comprobante import guardar_comprobante

router = APIRouter()

@router.post("/comprobante")
def registrar_comprobante(data: Comprobante, request: Request):
    verificar_token(request)
    return guardar_comprobante(
        ip=data.ip,
        referencia=data.referencia,
        telefono=data.telefono,
        cuenta=data.cuenta
    )
