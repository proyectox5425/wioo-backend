from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers import (
    validar,
    activar,
    comprobante,
    usuario,
    ticket,
    redireccionar,
    mi_ip
)

app = FastAPI(
    title="WIOO Backend",
    version="1.0.0",
    description="Sistema para gestión de WiFi en transporte público urbano"
)

# Seguridad CORS — reemplaza con tu dominio real
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://wioo.com.ve"],  # Ajustar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints raíz — visible para monitoreo
@app.get("/")
def index():
    return {
        "service": "WIOO Backend",
        "status": "online",
        "version": "1.0.0"
    }

# Conexión de routers — ya con tags si están definidos en cada archivo
app.include_router(validar.router)
app.include_router(activar.router)
app.include_router(comprobante.router)
app.include_router(usuario.router)
app.include_router(ticket.router)
app.include_router(redireccionar.router)
app.include_router(mi_ip.router)
