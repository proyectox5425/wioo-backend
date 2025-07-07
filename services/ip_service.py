from typing import Dict
import logging
import ipaddress

logger = logging.getLogger(__name__)

def procesar_ip(ip_raw: str) -> Dict:
    """
    Limpia y verifica si la IP es válida y pública.

    Args:
        ip_raw (str): IP cruda obtenida desde el request.

    Returns:
        dict: Resultado del análisis con tipo, estado y mensaje.
    """
    ip = ip_raw.strip()

    try:
        ip_obj = ipaddress.ip_address(ip)

        if ip_obj.is_private:
            tipo = "privada"
            estado = False
            mensaje = "⛔ IP privada detectada (no válida para activación)"
        elif ip_obj.version != 4:
            tipo = f"IPv{ip_obj.version}"
            estado = False
            mensaje = "⛔ Solo se acepta IPv4 pública"
        else:
            tipo = "pública"
            estado = True
            mensaje = "✅ IP
