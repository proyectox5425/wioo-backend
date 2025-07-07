from datetime import datetime, timedelta

def obtener_expiracion(minutos: int) -> datetime:
    return datetime.utcnow() + timedelta(minutes=minutos)

def tiempo_restante(expiracion: datetime) -> int:
    ahora = datetime.utcnow()
    delta = expiracion - ahora
    return max(int(delta.total_seconds() // 60), 0)

def esta_expirado(expiracion: datetime) -> bool:
    return datetime.utcnow() > expiracion
