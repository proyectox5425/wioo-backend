from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="WIOO Backend",
    version="1.0.0",
    description="Sistema para gestión de WiFi en transporte público urbano"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # cambiar después a dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from core.config import settings
from routers import (
    validar,
    activar,
    comprobante,
    usuario,
    ticket,
    redireccionar,
    mi_ip,
    pago_manual
)

@app.get("/")
def index():
    return {
        "service": "WIOO Backend",
        "status": "online",
        "version": "1.0.0"
    }

app.include_router(validar.router)
app.include_router(activar.router)
app.include_router(comprobante.router)
app.include_router(usuario.router)
app.include_router(ticket.router)
app.include_router(redireccionar.router)
app.include_router(mi_ip.router)
app.include_router(pago_manual.router)
