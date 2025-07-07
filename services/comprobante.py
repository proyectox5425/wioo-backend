from datetime import datetime
from database import cursor, conn
from typing import Dict
import logging

logger = logging.getLogger(__name__)

def guardar_comprobante(ip: str, referencia: str, telefono: str, cuenta: str) -> Dict:
    """
    Registra un comprobante bancario para la IP indicada.

    Args:
        ip (str): Dirección IP del usuario.
        referencia (str): Número de referencia del pago.
        telefono (str): Número telefónico vinculado al pago.
        cuenta (str): Cuenta de destino del pago.

    Returns:
        dict: Estado de registro y mensaje.
    """
    try:
        fecha_actual = datetime.utcnow().isoformat()
        cursor.execute("""
            INSERT INTO comprobantes (ip, referencia, telefono, cuenta, fecha)
            VALUES (?, ?, ?, ?, ?)
        """, (ip, referencia.strip(), telefono.strip(), cuenta.strip(), fecha_actual))
        conn.commit()
        return {
            "registrado": True,
            "mensaje": "✅ Comprobante recibido correctamente",
            "ip": ip,
            "referencia": referencia,
            "fecha": fecha_actual
        }
    except Exception as e:
        logger.error(f"Error al guardar comprobante para IP {ip}: {str(e)}")
        return {
            "registrado": False,
            "mensaje": "❌ Error al registrar comprobante",
            "error": str(e)
      }
