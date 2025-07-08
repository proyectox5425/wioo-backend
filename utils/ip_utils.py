import ipaddress

def es_ip_privada(ip: str) -> bool:
    """
    Verifica si una dirección IP es privada (ej. 192.168.X.X o 10.X.X.X).

    Args:
        ip (str): Dirección IP a evaluar.

    Returns:
        bool: True si es privada, False si no o si es inválida.
    """
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_private
    except ValueError:
        return False

def es_ip_valida(ip: str) -> bool:
    """
    Verifica si una cadena representa una dirección IP válida (IPv4 o IPv6).

    Args:
        ip (str): Cadena de IP a validar.

    Returns:
        bool: True si la IP es válida, False si no lo es.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
