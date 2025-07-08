import os
from dotenv import load_dotenv
from pydantic import BaseSettings, Field

# Verificamos que el archivo .env exista antes de cargarlo
if os.path.exists(".env"):
    load_dotenv()
else:
    print("⚠️ Archivo .env no encontrado. Usando valores por defecto.")

class Settings(BaseSettings):
    DB_URL: str = Field(..., env="DB_URL")
    JWT_SECRET: str = Field(..., env="JWT_SECRET")
    JWT_EXP_MINUTES: int = Field(60, env="JWT_EXP_MINUTES")
    HOST: str = Field("0.0.0.0", env="HOST")
    PORT: int = Field(8000, env="PORT")
    DEBUG: bool = Field(True, env="DEBUG")
    ENVIRONMENT: str = Field("dev", env="ENVIRONMENT")  # Puedes usar esto para condiciones en producción

    # Variables adicionales (opcional):
    QR_EXPIRATION_MINUTES: int = Field(10, env="QR_EXPIRATION_MINUTES")
    TOKEN_LENGTH: int = Field(6, env="TOKEN_LENGTH")

settings = Settings()
