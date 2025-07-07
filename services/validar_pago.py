from database import cursor
from typing import Dict
import logging

logger = logging.getLogger(__name__)

def verificar_pago(referencia: str) -> Dict:
    """
    Verifica si la referencia bancaria existe en la base de datos.

    Args:
        referencia (str): Número de referencia del comprobante.

    Returns:
        dict: Resultado de la verificación y mensaje.
    """
    try:
        cursor.execute(
            "SELECT fecha, ip, telefono, cuenta FROM comprobantes WHERE referencia = ?",
            (referencia.strip(),)
        )
        resultado = cursor.fetchone()

        if resultado:
            fecha, ip, telefono, cuenta = resultado
            return {
                "verificado": True,
                "mensaje": "✅ Referencia encontrada",
                "referencia": referencia,
                "fecha": fecha,
                "ip": ip,
                "telefono": telefono,
                "cuenta": cuenta
            }
        else:
            return {
                "verificado": False,
                "mensaje": "⛔ Referencia no encontrada",
                "referencia": referencia
            }
    except Exception as e:
        logger.error(f"Error al verificar referencia {referencia}: {str(e)}")
        return {
            "verificado": False,
            "mensaje": "❌ Error interno al verificar",
            "error": str(e)
        }
