from fastapi import FastAPI

from routers.clientes import router_clientes
from routers.facturas import router_facturas
from routers.transacciones import router_transacciones

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}

# Routers
app.include_router(router_clientes)
app.include_router(router_facturas)
app.include_router(router_transacciones)