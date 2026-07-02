from pydantic import BaseModel
from typing import Optional
from datetime import date

class Aposta(BaseModel):
    valor: int 
    data: Optional[date] = None
    cpf_usuario: int
    id_bolao: int 

class ApotaUpadate(BaseModel): 
    valor: int
    data: Optional[date] = None

class Campeonato(BaseModel): 
    nome_campeonato: str
    ano: int

class CampeonatoUpadate(BaseModel): 
    nome_campeonato: str
    ano: int
