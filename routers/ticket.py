from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List, Dict, Union

from database import get_db
from models import Boleto
from schemas import TicketResponse, TicketResumenResponse

router = APIRouter()

@router.get("/tickets", response_model=Union[Dict[str, Union[int, List[TicketResponse]]], List[TicketResponse]])
def obtener_tickets_por_chofer(
    codigo_chofer: str,
    incluir_resumen: bool = True,
    dias: int = 7,
    db: Session = Depends(get_db)
):
    fecha_inicio = datetime.utcnow() - timedelta(days=dias)
    
    boletos = db.query(Boleto).filter(
        Boleto.codigo_chofer == codigo_chofer,
        Boleto.fecha >= fecha_inicio
    ).all()
    
    if incluir_resumen:
        monto_unitario = 150  # Valor del boleto en Bs
        resumen = {
            "total": len(boletos),
            "monto_recaudado": len(boletos) * monto_unitario,
            "tickets": boletos
        }
        return resumen
    return boletos
