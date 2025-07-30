from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from config.db_supabase import supabase_client  # cliente Supabase ya configurado

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
    # 🔎 Validación visual mínima
    if len(datos.telefono) < 10:
        raise HTTPException(status_code=400, detail="Teléfono inválido")

    if not datos.referencia or datos.monto <= 0:
        raise HTTPException(status_code=400, detail="Datos incompletos")

    # 🔁 Detección de duplicado por referencia
    duplicado = supabase_client.table("pago_manual").select("id").eq("referencia", datos.referencia).execute()
    if duplicado.data:
        raise HTTPException(status_code=409, detail="Referencia ya registrada")

    # 📝 Registro limpio
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

    if not resultado.data:
        raise HTTPException(status_code=500, detail="Error al registrar comprobante")

    return {
        "estado": "pendiente",
        "mensaje": "✅ Comprobante registrado correctamente. Esperando validación."
    }

@router.post("/api/aprobar-comprobante")
async def aprobar_comprobante(data: dict):
    id_comprobante = data.get("id")
    if not id_comprobante:
        raise HTTPException(status_code=400, detail="Falta el ID del comprobante")

    # ✅ Actualiza estado en Supabase
    respuesta = supabase_client.table("pago_manual") \
        .update({"estado": "aprobado", "fecha_validacion": datetime.utcnow().isoformat()}) \
        .eq("id", id_comprobante).execute()

    if not respuesta.data:
        raise HTTPException(status_code=500, detail="❌ No se pudo aprobar el comprobante")

    # 🧩 Activación opcional de servicio si tenés un flujo técnico con Mikrotik
    # activar_wifi_para_dispositivo(id_comprobante)

    return {
        "estado": "aprobado",
        "mensaje": "✅ Comprobante validado manualmente"
    }

@router.post("/api/rechazar-comprobante")
async def rechazar_comprobante(data: dict):
    id_comprobante = data.get("id")
    motivo = data.get("motivo", "Rechazo manual")

    if not id_comprobante:
        raise HTTPException(status_code=400, detail="Falta el ID del comprobante")

    # ❌ Registro institucional de rechazo
    respuesta = supabase_client.table("pago_manual") \
        .update({
            "estado": "rechazado",
            "fecha_validacion": datetime.utcnow().isoformat(),
            "motivo_rechazo": motivo
        }) \
        .eq("id", id_comprobante).execute()

    if not respuesta.data:
        raise HTTPException(status_code=500, detail="❌ No se pudo rechazar el comprobante")

    return {
        "estado": "rechazado",
        "mensaje": "❌ Comprobante rechazado manualmente"
        }
