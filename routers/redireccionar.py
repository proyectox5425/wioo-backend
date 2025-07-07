from fastapi import APIRouter, Request
from database import cursor
from datetime import datetime
from fastapi.responses import RedirectResponse
from core.security import verificar_token  # 👈 Verificación
from fastapi import Query  # 👈 Para extraer el parámetro 'ip'

router = APIRouter()

@router.get("/redireccionar")
def redireccionar_por_ip(ip: str = Query(...), request: Request = None):
    verificar_token(request)  # 🔐 Exige token válido
    cursor.execute("SELECT expiracion FROM tickets WHERE ip = ?", (ip,))
    resultado = cursor.fetchone()

    if resultado:
        expiracion = datetime.fromisoformat(resultado[0])
        if expiracion > datetime.utcnow():
            return RedirectResponse(url="/aprobado.html")

    return RedirectResponse(url="/rechazado.html")
