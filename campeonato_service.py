from fastapi import APIRouter, HTTPException
from db import get_connection
from models import Campeonato, CampeonatoUpadate
from typing import List, Optional

router = APIRouter()

@router.post("/campeonatos")
async def criar_aposta(dto: Campeonato):
    conn = get_connection()
    cur = conn.cursor()

    try: 
        cur.execute(
            "INSERT INTO campeonato(nome_campeonato, ano) VALUES (%d, %d)",
            (dto.nome_campeonato, dto.ano)
        )
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(400, f"Erro ao criar um campeonato {e}")
    
    finally:
        cur.close()
        conn.close()
    return {"msg":"Campeonato criado com sucesso!"}


