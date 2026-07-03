from pydantic import BaseModel
from typing import Optional
from datetime import date

class Aposta(BaseModel):
    id_aposta: Optional[int] = None
    valor: int
    data: Optional[date] = None
    cpf_usuario: str
    id_bolao: int

class ApostaUpdate(BaseModel): 
    valor: Optional[int] = None
    data: Optional[date] = None


# class Campeonato(BaseModel): 
#     nome_campeonato: str
#     ano: int

# class CampeonatoUpadate(BaseModel): 
#     nome_campeonato: str
#     ano: int
