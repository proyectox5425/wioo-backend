from datetime import datetime, timedelta
from utils.insertar_ticket import insertar_ticket
from utils.logger import logger
from fastapi.responses import JSONResponse
import traceback

def activar_ip(IP: str, metodo_pago: str = "desconocido") -> JSONResponse:
    fecha_actual = datetime.utcnow()
    duracion_horas = 24

    try:
        # Registrar ticket de activación (puede incluir más campos si tienes usuario)
        ticket = insertar_ticket(
            ip=IP,
            duracion=duracion_horas,
            fecha=fecha_actual,
            metodo_pago=metodo_pago
        )

        logger.info(
            f"[{fecha_actual.isoformat()}] Activación registrada para IP {IP} con ticket ID {ticket.get('id', 'N/A')}"
        )

        return JSONResponse(
            status_code=200,
            content={
                "mensaje": "Acceso activado por 24 horas.",
                "ip": IP,
                "duracion_horas": duracion_horas,
                "ticket": ticket
            }
        )

    except Exception as e:
        logger.error(
            f"[{fecha_actual.isoformat()}] Error al activar IP {IP} → {repr(e)}\n{traceback.format_exc()}"
        )
        return JSONResponse(
            status_code=500,
            content={"error": "Hubo un problema al activar el acceso. Intenta nuevamente más tarde."}
        )
