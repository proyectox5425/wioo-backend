from database import cursor
from datetime import datetime
from typing import Dict, Any
import logging
import traceback

logger = logging.getLogger(__name__)

def estadisticas_por_dia(fecha: str) -> Dict[str, Any]:
    """
    Devuelve la cantidad de validaciones por método en una fecha específica.

    Args:
        fecha (str): Fecha en formato 'YYYY-MM-DD'

    Returns:
        dict: Conteo por método y total del día.
    """
    try:
        cursor.execute("""
            SELECT metodo_pago, COUNT(*)
            FROM tickets
            WHERE DATE(hora_activacion) = ?
            GROUP BY metodo_pago
        """, (fecha.strip(),))
        resultados = cursor.fetchall()

        conteos = {metodo: cantidad for metodo, cantidad in resultados}
        total = sum(conteos.values())

        return {
            "fecha": fecha,
            "conteo_por_metodo": conteos,
            "total": total
        }

    except Exception as e:
        logger.error(f"Error en estadisticas para {fecha}: {traceback.format_exc()}")
        return {
            "mensaje": "❌ No se pudo calcular las estadísticas",
            "error": str(e)
        }
