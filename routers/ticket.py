from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from modelos.ticket import Boleto
from esquemas.ticket_schema import TicketResponse
from base_de_datos import get_db

router = APIRouter()

@router.get("/tickets", response_model=List[TicketResponse])
def obtener_tickets_por_chofer(codigo_chofer: str, db: Session = Depends(get_db)):
    boletos = db.query(Boleto).filter(Boleto.codigo_chofer == codigo_chofer).all()
    return boletos
