from datetime import datetime
from utils.insertar_ip import insertar_ip
from utils.logger import logger
from fastapi.responses import JSONResponse
import traceback

def registrar_ip(ip: str, usuario_id: int) -> JSONResponse:
    fecha_actual = datetime.utcnow()

    try:
        ip_registrada = insertar_ip(
            ip=ip,
            fecha=fecha_actual,
            usuario_id=usuario_id
        )

        logger.info(
            f"[{fecha_actual.isoformat()}] IP registrada → IP={ip} | UsuarioID={usuario_id}"
        )

        return JSONResponse(
            status_code=200,
            content={
                "mensaje": "IP registrada correctamente.",
                "ip": ip,
                "usuario_id": usuario_id,
                "registro": ip_registrada
            }
        )

    except Exception as e:
        logger.error(
            f"[{fecha_actual.isoformat()}] Error al registrar IP={ip} | UsuarioID={usuario_id}\n{repr(e)}\n{traceback.format_exc()}"
        )

        return JSONResponse(
            status_code=500,
            content={
                "error": "No se pudo registrar la IP.",
                "detalle": str(e)
            }
        )
