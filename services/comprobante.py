from datetime import datetime
from utils.insertar_comprobante import insertar_comprobante
from utils.logger import logger
from fastapi.responses import JSONResponse
import traceback

def crear_comprobante(ticket_id: int, usuario_id: int, estado: str = "pendiente") -> JSONResponse:
    fecha_actual = datetime.utcnow()

    try:
        comprobante = insertar_comprobante(
            ticket_id=ticket_id,
            usuario_id=usuario_id,
            estado=estado,
            fecha=fecha_actual
        )

        logger.info(
            f"[{fecha_actual.isoformat()}] Comprobante creado → TicketID={ticket_id} | UsuarioID={usuario_id} | Estado={estado}"
        )

        return JSONResponse(
            status_code=200,
            content={
                "mensaje": "Comprobante registrado correctamente.",
                "comprobante": comprobante
            }
        )

    except Exception as e:
        logger.error(
            f"[{fecha_actual.isoformat()}] Error al crear comprobante → TicketID={ticket_id} | UsuarioID={usuario_id} | Estado={estado}\n{repr(e)}\n{traceback.format_exc()}"
        )

        return JSONResponse(
            status_code=500,
            content={
                "error": "No se pudo registrar el comprobante.",
                "detalle": str(e)
            }
        )
