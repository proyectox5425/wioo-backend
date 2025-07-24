from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from dependencias import get_db
from token_utils import crear_token
from modelos import Usuario  # Asegúrate de tener tu modelo de usuario
from esquemas import LoginIn, LoginOut  # Puedes definirlos si no existen aún

router = APIRouter()

@router.post("/login", response_model=LoginOut)
def login(datos: LoginIn, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.usuario == datos.usuario).first()

    if not usuario or not usuario.clave == datos.clave:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")

    token = crear_token({
        "sub": usuario.id,
        "rol": usuario.rol,
        "usuario": usuario.usuario
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "rol": usuario.rol
                                       }
