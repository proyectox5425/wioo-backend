from database import cursor
from typing import Dict, Any
import logging
import traceback

logger = logging.getLogger(__name__)

def verificar_referencia(referencia: str) -> Dict[str, Any]:
    """
    Verifica si una referencia bancaria existe en la base de datos.

    Args:
        referencia (str): Código de referencia del comprobante.

    Returns:
        Dict[str, Any]: Resultado de la verificación y los datos si se encontró.
    """
    try:
        # Limpieza del dato de entrada
        referencia = referencia.strip()

        cursor.execute("""
            SELECT fecha, ip, telefono, cuenta
            FROM comprobantes
            WHERE referencia = ?
        """, (referencia,))
        resultado = cursor.fetchone()

        if resultado:
            fecha, ip, telefono, cuenta = resultado
            return {
                "verificado": True,
                "mensaje": "✓ Referencia encontrada",
                "referencia": referencia,
                "fecha": fecha,
                "ip": ip,
                "telefono": telefono,
                "cuenta": cuenta
            }
        else:
            return {
                "verificado": False,
                "mensaje": "🚫 Referencia no encontrada"
            }

    except Exception as e:
        logger.error(f"Error al verificar referencia {referencia}: {traceback.format_exc()}")
        return {
            "verificado": False,
            "mensaje": "❌ Error interno al verificar",
            "error": str(e)
            }
