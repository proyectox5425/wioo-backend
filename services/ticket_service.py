from datetime import datetime, timedelta
from database import cursor, conn
from typing import Dict
import logging

logger = logging.getLogger(__name__)

# Duración del ticket en horas (puede ajustarse por configuración externa)
DURACION_HORAS = 24

def generar_ticket(ip: str, metodo_pago: str = "efectivo") -> Dict:
    """
    Genera un ticket válido por duración definida, y lo guarda en la base de datos.

    Args:
        ip (str): Dirección IP del usuario.
        metodo_pago (str): Forma de activación (ej. efectivo, emergencia).

    Returns:
        dict: Estado de la creación y expiración calculada.
    """
    try:
        ahora = datetime.utcnow()
        expiracion = ahora + timedelta(hours=DURACION_HORAS)

        cursor.execute("""
            INSERT INTO tickets (ip, metodo_pago, hora_activacion, expiracion)
            VALUES (?, ?, ?, ?)
        """, (ip, metodo_pago, ahora.isoformat(), expiracion.isoformat()))
        conn.commit()

        return {
            "generado": True,
            "ip": ip,
            "metodo": metodo_pago,
            "expira_en": expiracion.isoformat()
        }
    except Exception as e:
        logger.error(f"Error al generar ticket para IP {ip}: {str(e)}")
        return {
            "generado": False,
            "mensaje": "❌ No se pudo generar el ticket",
            "error": str(e)
        }
