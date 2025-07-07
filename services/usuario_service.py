from utils.token_utils import crear_token
from database import cursor
from typing import Dict
import logging

logger = logging.getLogger(__name__)

def autenticar_usuario(usuario: str, clave: str) -> Dict:
    """
    Verifica si el usuario existe y su clave es correcta.

    Args:
        usuario (str): Nombre o ID del usuario.
        clave (str): Contraseña ingresada.

    Returns:
        dict: Token generado si es válido, con rol y mensaje.
    """
    try:
        cursor.execute("""
            SELECT rol FROM usuarios WHERE usuario = ? AND clave = ?
        """, (usuario.strip(), clave.strip()))
        resultado = cursor.fetchone()

        if resultado:
            rol = resultado[0]
            token = crear_token(usuario, rol)
            return {
                "autenticado": True,
                "mensaje": "✅ Acceso concedido",
                "usuario": usuario,
                "rol": rol,
                "token": token
            }
        else:
            return {
                "autenticado": False,
                "mensaje": "⛔ Usuario o clave incorrecta"
            }
    except Exception as e:
        logger.error(f"Error al autenticar usuario {usuario}: {str(e)}")
        return {
            "autenticado": False,
            "mensaje": "❌ Error interno al autenticar",
            "error": str(e)
          }
