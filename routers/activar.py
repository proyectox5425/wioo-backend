from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.activar_schema import ActivarCreate, ActivarOut
from services.activar import activar_usuario
from core.database import get_db
from utils.token_utils import verificar_token_rol

router = APIRouter()

@router.post("/activar", response_model=ActivarOut, tags=["Activar"])
def activar_entidad(
    data: ActivarCreate,
    db: Session = Depends(get_db),
    usuario: dict = Depends(verificar_token_rol)
):
    """
    Activa el acceso de un usuario por duración configurada.
    Protegido por token JWT (roles: admin, chofer).
    """
    rol = usuario["rol"]
    usuario_token_id = usuario["usuario"]

    # Restricción opcional: si no eres admin, solo puedes activar para ti
    if rol != "admin" and data.usuario_id != usuario_token_id:
        raise HTTPException(status_code=403, detail="🚫 No puedes activar para otro usuario")

    try:
        resultado = activar_usuario(data, db)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error al activar: {str(e)}")
