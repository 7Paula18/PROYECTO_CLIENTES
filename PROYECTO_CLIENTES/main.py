from fastapi import FastAPI
from modelos.clientes import Cliente, ClienteCrear
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"Hola mundo"}


lista_clientes:list[Cliente] = []

class Cliente(BaseModel):
    id:int
    nombre:str
    edad:int
    descripcion:str

@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}

@app.post("/clientes", response_model=Cliente)
async def crear_clientes(datos_cliente : ClienteCrear):
    #validar datos cliente
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #asignar id al cliente
    cliente_val.id = len(lista_clientes)+1
    #agregar a lista de clientes
    lista_clientes.append(cliente_val)
    #retornar el dato del cliente agregado
    return cliente_val

#editar put y delete, con "response_model=Cliente" y el return

@app.get("/cliente/{cliente_id}")
def obtener_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            return cliente
    return {"error" : "Cliente no encontrado"}


@app.put("/clientes/{id}", response_model=Cliente)
async def editar_cliente(id: int, datos_cliente: ClienteCrear):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
                cliente_val = Cliente.model_validate(datos_cliente.model_dump())
                cliente_val.id = id
                lista_clientes[i] = cliente_val
                return cliente_val
    return{"mensaje":"Cliente no encontrado"}

@app.delete("/clientes/{id}", response_model=Cliente)
def eliminar_clientes(id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            eliminado = lista_clientes.pop(i)
            return eliminado
    return {"mensaje": "Cliente no encontrado"}