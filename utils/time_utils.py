from datetime import datetime, timedelta

def obtener_expiracion(minutos: int) -> datetime:
    """
    Calcula la fecha y hora de expiración actual sumando X minutos.

    Args:
        minutos (int): Cantidad de minutos hasta expirar.

    Returns:
        datetime: Momento de expiración en UTC.
    """
    return datetime.utcnow() + timedelta(minutes=minutos)

def tiempo_restante(expiracion: datetime) -> int:
    """
    Devuelve cuántos minutos faltan para que algo expire.

    Args:
        expiracion (datetime): Tiempo límite a evaluar.

    Returns:
        int: Minutos restantes. Devuelve 0 si ya expiró.
    """
    ahora = datetime.utcnow()
    delta = expiracion - ahora
    return max(int(delta.total_seconds() // 60), 0)

def esta_expirado(expiracion: datetime) -> bool:
    """
    Verifica si un tiempo dado ya está vencido.

    Args:
        expiracion (datetime): Momento de expiración a evaluar.

    Returns:
        bool: True si ya venció, False si aún es válido.
    """
    return datetime.utcnow() > expiracion
