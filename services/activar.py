from database import insertar_ticket
from typing import Dict
import logging

logger = logging.getLogger(__name__)

def activar_ip(ip: str, metodo_pago: str = "desconocido") -> Dict:
    """
    Activa el acceso para una IP durante 24 horas.
    
    Args:
        ip (str): Dirección IP del usuario.
        metodo_pago (str): Método utilizado para activar (ej. efectivo, transferencia).

    Returns:
        dict: Estado de activación y mensaje correspondiente.
    """
    try:
        insertar_ticket(ip=ip, metodo_pago=metodo_pago)
        return {
            "activado": True,
            "mensaje": "✅ Acceso activado por 24 horas",
            "ip": ip,
            "metodo_pago": metodo_pago
        }
    except Exception as e:
        logger.error(f"Error al activar IP {ip}: {str(e)}")
        return {
            "activado": False,
            "mensaje": "❌ No se pudo activar el acceso",
            "error": str(e)
        }
