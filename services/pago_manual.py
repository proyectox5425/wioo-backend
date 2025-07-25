from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()  # 🔐 Carga tus variables del archivo .env

# 📡 Conexión institucional a Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def registrar_pago_manual(datos: dict) -> bool:
    respuesta = supabase.table("pago_manual").insert(datos).execute()
    return respuesta.status_code == 201
