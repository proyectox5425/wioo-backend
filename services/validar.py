from database import cursor
from datetime import datetime
from typing import Dict, Any
import logging
import traceback

logger = logging.getLogger(__name__)

def validar_ip(ip: str) -> Dict[str, Any]:
    """
    Valida si una dirección IP tiene un ticket activo y no expirado.

    Args:
        ip (str): Dirección IP a validar.

    Returns:
        dict: Resultado con autorización y mensaje detallado.
    """
    try:
        ahora = datetime.utcnow()

        cursor.execute("""
            SELECT hora_activacion, expiracion
            FROM tickets
            WHERE ip = ?
            ORDER BY hora_activacion DESC
            LIMIT 1
        """, (ip.strip(),))
        resultado = cursor.fetchone()

        if resultado:
            hora_activacion, expiracion = resultado

            if ahora > expiracion:
                return {
                    "autorizado": False,
                    "detalle": "❌ Ticket vencido",
                    "expiracion": expiracion.isoformat()
                }

            return {
                "autorizado": True,
                "detalle": "✅ Acceso válido",
                "ip": ip,
                "hora_activacion": hora_activacion.isoformat(),
                "expiracion": expiracion.isoformat()
            }
        else:
            return {
                "autorizado": False,
                "detalle": "🚫 No existe un ticket para esta IP"
            }

    except Exception as e:
        logger.error(f"Error validando IP {ip}: {traceback.format_exc()}")
        return {
            "autorizado": False,
            "detalle": "❌ Error interno al validar",
            "error": str(e)
            }
