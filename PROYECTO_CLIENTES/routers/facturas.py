from fastapi import APIRouter
from modelos.facturas import Factura

router_facturas = APIRouter()

lista_facturas: list[Factura] = []

# =========================
# LISTAR FACTURAS
# =========================

@router_facturas.get("/facturas")
def listar_facturas():
    return {"facturas": lista_facturas}

# =========================
# CREAR FACTURA
# =========================

@router_facturas.post("/facturas")
def crear_factura(factura: Factura):

    lista_facturas.append(factura)

    return factura