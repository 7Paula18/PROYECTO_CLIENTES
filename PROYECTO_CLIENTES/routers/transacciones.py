from fastapi import APIRouter
from modelos.transacciones import Transaccion

router_transacciones = APIRouter()

lista_transacciones: list[Transaccion] = []

# =========================
# LISTAR
# =========================

@router_transacciones.get("/transacciones")
def listar_transacciones():
    return {"transacciones": lista_transacciones}

# =========================
# CREAR
# =========================

@router_transacciones.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):

    lista_transacciones.append(transaccion)

    return transaccion