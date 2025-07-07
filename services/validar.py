from database import cursor
from datetime import datetime
from typing import Dict
import logging

logger = logging.getLogger(__name__)

def validar_ip(ip: str) -> Dict:
    """
    Valida si la IP tiene un ticket activo y no vencido.

    Args:
        ip (str): Dirección IP del usuario.

    Returns:
        dict: Resultado de la validación, incluyendo detalle de estado.
    """
    try:
        cursor.execute("SELECT hora_activacion, expiracion FROM tickets WHERE ip = ?", (ip,))
        resultado = cursor.fetchone()

        if not resultado:
            return {"autorizado": False, "detalle": "⛔ No hay ticket para esta IP"}

        hora_activacion, expiracion_str = resultado

        if not hora_activacion or not expiracion_str:
            return {"autorizado": False, "detalle": "⛔ Ticket incompleto (no activado)"}

        expiracion = datetime.fromisoformat(expiracion_str)
        ahora = datetime.utcnow()

        if ahora > expiracion:
            return {"autorizado": False, "detalle": "⛔ Ticket vencido"}

        return {"autorizado": True, "detalle": "✅ IP autorizada", "expira_en": expiracion.isoformat()}

    except Exception as e:
        logger.error(f"Error al validar IP {ip}: {str(e)}")
        return {"autorizado": False, "detalle": "❌ Error interno al validar", "error": str(e)}
