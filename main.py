from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import validar
from routers import activar
from routers import comprobante
from routers import redireccionar
from routers import mi_ip  # 👈 Nuevo router para detectar IP real

from dotenv import load_dotenv
import os

# Cargar las variables desde el archivo .env
from core.config import settings
TOKEN_SECRETO = settings.TOKEN_SECRETO

app = FastAPI(
    title="Backend WiFi Bus",
    version="1.0",
    description="API para validar accesos al portal WiFi del bus"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔐 En producción puedes limitar esto por dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de routers
app.include_router(validar.router)
app.include_router(activar.router)
app.include_router(comprobante.router)
app.include_router(redireccionar.router)
app.include_router(mi_ip.router)

@app.get("/")
def bienvenida():
    return {
        "mensaje": "¡Hola Ysai! Tu backend está funcionando 💻🔥"
    }
    if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
)
