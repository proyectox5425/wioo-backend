import os
from dotenv import load_dotenv

# 📦 Cargamos las variables desde el archivo .env
load_dotenv()

# 🔐 Seguridad JWT
JWT_SECRET = os.getenv("JWT_SECRET", "clave-predeterminada")
JWT_EXP_MIN = int(os.getenv("JWT_EXP_MIN", "60"))

# 🗃️ Base de datos
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "wifi_bus_db")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123")

# 📤 Email
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

# 📊 Otros
TIMEZONE = os.getenv("TIMEZONE", "America/Caracas")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
