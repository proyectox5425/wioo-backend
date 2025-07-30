from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from config.db_supabase import supabase_client  # tu cliente ya configurado

router = APIRouter()

class ComprobanteCreate(BaseModel):
    telefono: str
    banco: str
    referencia: str
    monto: float
    unidad: str
    metodo: str
    ash_dispositivo: str

@router.post("/api/cargar-comprobante")
async def cargar_comprobante(datos: ComprobanteCreate):
    # Validación básica visual
    if len(datos.telefono) < 10:
        raise HTTPException(status_code=400, detail="Teléfono inválido")

    if not datos.referencia or datos.monto <= 0:
        raise HTTPException(status_code=400, detail="Datos incompletos")

    # Detección de duplicado por referencia
    duplicado = supabase_client.table("pago_manual").select("id").eq("referencia", datos.referencia).execute()
    if duplicado.data:
        raise HTTPException(status_code=409, detail="Referencia ya registrada")

    # Registro limpio
    nuevo = {
        "telefono": datos.telefono,
        "banco": datos.banco,
        "referencia": datos.referencia,
        "monto": datos.monto,
        "unidad": datos.unidad,
        "metodo": datos.metodo,
        "estado": "pendiente",
        "fecha_hora": datetime.utcnow().isoformat(),
        "ash_dispositivo": datos.ash_dispositivo
    }

    resultado = supabase_client.table("pago_manual").insert(nuevo).execute()

    if resultado.status_code != 201:
        raise HTTPException(status_code=500, detail="Error al registrar comprobante")

    return {
    "estado": "pendiente",
    "mensaje": "✅ Comprobante registrado correctamente. Esperando validación."
    }
