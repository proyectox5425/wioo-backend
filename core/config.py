from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    # 🔐 Seguridad
    JWT_SECRET: str = os.getenv("JWT_SECRET", "default_jwt_secret")
    BANCO_API_URL: str = os.getenv("BANCO_API_URL", "")
    BANCO_API_KEY: str = os.getenv("BANCO_API_KEY", "")

    # 🌐 Configuración del servidor
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # 🛢️ Base de datos
    DB_PATH: str = os.getenv("DB_PATH", "accesos.db")

    # 🚌 Identificador único del autobús
    BUS_ID: str = os.getenv("BUS_ID", "UNDEFINED")

    # 💳 Validación de comprobantes bancarios
    VALIDAR_COMPROBANTES: bool = os.getenv("VALIDAR_COMPROBANTES", "False").lower() == "true"

    # ⏳ Configuración de expiración de tickets
    TICKET_EXPIRACION_MINUTOS: int = int(os.getenv("TICKET_EXPIRACION_MINUTOS", "10"))

settings = Settings()
