from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    correo = Column(String, unique=True, index=True)  # ✅ Evita duplicados y mejora búsquedas
    contrasena = Column(String)
    rol = Column(String, index=True)  # ✅ Index para filtrar por tipo de usuario
    activo = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Usuario correo={self.correo} rol={self.rol}>"
