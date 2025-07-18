from database import cursor
from typing import Dict, Optional, Any
import logging
from datetime import datetime
import traceback

logger = logging.getLogger(__name__)

def obtener_anuncio_para_ip(ip: str, zona: Optional[str] = None) -> Dict[str, Any]:
    """
    Selecciona el anuncio correspondiente para una IP, de forma dinámica.

    Args:
        ip (str): Dirección IP del usuario.
        zona (Optional[str]): Zona geográfica o ruta del bus (opcional).

    Returns:
        dict: Datos del anuncio: imagen, texto, empresa, duración, etc.
    """
    try:
        hora_actual = datetime.utcnow().hour

        if 6 <= hora_actual < 10:
            categoria = "desayuno"
        elif 11 <= hora_actual < 14:
            categoria = "almuerzo"
        elif 17 <= hora_actual < 20:
            categoria = "servicios"
        else:
            categoria = "general"

        cursor.execute("""
            SELECT imagen_url, texto_promocional, empresa, duracion_segundos
            FROM anuncios
            WHERE categoria = ?
            ORDER BY RANDOM()
            LIMIT 1
        """, (categoria,))
        resultado = cursor.fetchone()

        if resultado:
            imagen_url, texto, empresa, duracion = resultado
            return {
                "mostrar": True,
                "categoria": categoria,
                "empresa": empresa,
                "imagen": imagen_url,
                "mensaje": texto,
                "duracion": duracion
            }

        return {
            "mostrar": False,
            "mensaje": "🚫 No hay anuncios disponibles en esta categoría"
        }

    except Exception as e:
        logger.error(f"Error al obtener anuncio para IP {ip}: {traceback.format_exc()}")
        return {
            "mostrar": False,
            "mensaje": "❌ Error interno al cargar anuncio",
            "error": str(e)
        }
