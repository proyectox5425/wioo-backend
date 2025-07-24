from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.usuario_schema import UsuarioLogin
from models.usuario import Usuario
from utils.token_utils import crear_token
from dependencias import get_db

router = APIRouter()

@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.correo == datos.correo).first()

    if not usuario or usuario.contrasena != datos.contrasena:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="⛔ Credenciales inválidas")

    token = crear_token({
        "sub": usuario.id,
        "rol": usuario.rol,
        "correo": usuario.correo
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "rol": usuario.rol
}
