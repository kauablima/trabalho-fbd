from fastapi import APIRouter, HTTPException
from db import get_connection
from models import Aposta, ApostaUpdate
from typing import List, Optional

router = APIRouter()

@router.post("/apostas")
async def criar_aposta(dto: Aposta):
    conn = get_connection()
    cur = conn.cursor()

    try: 
        cur.execute(
            "INSERT INTO aposta(valor, data, cpf_usuario, id_bolao) VALUES(%s, %s, %s, %s)",
            (dto.valor, dto.data, dto.cpf_usuario, dto.id_bolao)
        )

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(400, f"Erro ao criar uma aposta {e}")
    
    finally:
        cur.close()
        conn.close()
    return {"msg":"Aposta criada com sucesso!"}


@router.get("/apostas")
async def listar_apostas():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT  id_aposta, valor, data, cpf_usuario, id_bolao FROM aposta"
    )

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [
        Aposta(
            id_aposta=a[0],
            valor=a[1], 
            data=a[2] , 
            cpf_usuario=a[3], 
            id_bolao=a[4]
        ) for a in rows 
    ]

@router.get("/apostas/{id_aposta}")   
async def listar_aposta_by_id(id_aposta: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id_aposta, valor, data, cpf_usuario, id_bolao FROM aposta WHERE id_aposta=%s", (id_aposta,)
    )

    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return Aposta(
            id_aposta=row[0],
            valor=row[1],
            data=row[2], 
            cpf_usuario=row[3], 
            id_bolao=row[4]
        )
    raise HTTPException(404, f"Não possui nenhuma aposta registrada")

@router.patch("/apostas/{id_aposta}")
async def atualizar_aposta(id_aposta: int, dto: ApostaUpdate):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id_aposta FROM aposta WHERE id_aposta=%s", (id_aposta,)
    )

    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(404, f"Aposta não encontrada")

    fields = []
    values = []

    for campo, valor in dto.dict(exclude_unset=True).items():
        fields.append(f"{campo}=%s")
        values.append(valor)

    if not fields:
        cur.close()
        conn.close()
        raise HTTPException(404, f"Nenhum campo informado na atualização")

    values.append(id_aposta)
    
    try:
        cur.execute(
            f"UPDATE aposta SET {', '.join(fields)} WHERE id_aposta=%s", values
        )
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(400, f"Erro ao atualizar uma aposta {e}")
    finally:
        cur.close()
        conn.close()
    return {"msg":"Aposta atualizada com sucesso!"}

@router.delete("/apostas/{id_aposta}")
async def deletar_aposta(id_aposta: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM aposta WHERE id_aposta=%s", (id_aposta,)) 
    conn.commit()
    cur.close()
    conn.close()

    return {"msg": "Aposta deletada com sucesso!"}