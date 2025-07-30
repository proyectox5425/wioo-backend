from fastapi import APIRouter
from datetime import datetime
from database import db
from modelos.pago_manual import PagoManualIn
from modelos.ticket import Ticket
from services.pago_manual import registrar_pago_manual

router = APIRouter()

@router.post("/api/cargar-comprobante")
def cargar_comprobante(datos: PagoManualIn):
    datos_dict = datos.dict()

    if not datos_dict.get("fecha_hora"):
        datos_dict["fecha_hora"] = datetime.utcnow().isoformat()

    resultado = registrar_pago_manual(datos_dict)

    if resultado:
        # Crear ticket institucional para trazabilidad
        ticket = Ticket(
            usuario_id=None,
            codigo=datos.referencia,
            metodo="pago_manual",
            estado="pendiente",
            fecha=datetime.utcnow(),
            unidad=datos.unidad,
            chofer=None,
            banco=datos.banco,
            monto=datos.monto
        )
        db.add(ticket)
        db.commit()

        return {
            "estado": "pendiente",
            "referencia": datos.referencia,
            "unidad": datos.unidad,
            "banco": datos.banco,
            "monto": datos.monto,
            "fecha": datos_dict["fecha_hora"],
            "ticket_id": ticket.id
        }

    else:
        return { "estado": "rechazado" }
