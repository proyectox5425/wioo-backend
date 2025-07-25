from fastapi import APIRouter
from schemas.pago_manual import PagoManualIn
from services.pago_manual import registrar_pago_manual
from datetime import datetime

router = APIRouter()

@router.post("/api/cargar-comprobante")
def cargar_comprobante(datos: PagoManualIn):
    datos_dict = datos.dict()
    
    # Añadir fecha_hora si no viene desde frontend
    if "fecha_hora" not in datos_dict or not datos_dict["fecha_hora"]:
        datos_dict["fecha_hora"] = datetime.utcnow()

    resultado = registrar_pago_manual(datos_dict)

    if resultado:
        return { "estado": "pendiente" }
    else:
        return { "estado": "rechazado" }
