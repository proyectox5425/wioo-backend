from services.validar_service import validar_ip
from services.verificar_pago_service import verificar_pago
from typing import Dict
import logging
import traceback
from database import get_db_connection  # Si tienes acceso directo a SQLite

logger = logging.getLogger(__name__)

def evaluar_redireccion(ip: str) -> Dict:
    """
    Determina si una IP puede acceder al internet según su método de validación.

    Args:
        ip (str): Dirección IP del usuario.

    Returns:
        dict: Resultado con estado final, mensaje visual y código.
    """
    try:
        # 🔐 Validar ticket activo
        resultado_ticket = validar_ip(ip)
        if resultado_ticket.get("autorizado"):
            return {
                "acceso": True,
                "estado": "aprobado",
                "mensaje": "✅ Acceso permitido por ticket",
                "expira_en": resultado_ticket.get("expira_en")
            }

        # 🔎 Validar comprobante de pago
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT referencia FROM comprobantes WHERE ip = ?", (ip,))
        resultado_pago = cursor.fetchone()
        conn.close()

        if resultado_pago:
            return {
                "acceso": False,
                "estado": "pendiente",
                "mensaje": "⏳ Comprobante recibido. Esperando aprobación.",
                "referencia": resultado_pago[0]
            }

        # ❌ Ninguna validación encontrada
        return {
            "acceso": False,
            "estado": "rechazado",
            "mensaje": "⛔ No se encontró validación activa. Debe pagar o usar ticket."
        }

    except Exception as e:
        logger.error(
            f"[{ip}] Error en evaluación de redirección → {repr(e)}\n{traceback.format_exc()}"
        )
        return {
            "acceso": False,
            "estado": "error",
            "mensaje": "❌ Error interno al evaluar acceso",
            "error": str(e)
        }
