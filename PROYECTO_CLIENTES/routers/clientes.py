from fastapi import APIRouter
from modelos.clientes import Cliente, ClienteCrear

router_clientes = APIRouter()

# Base de datos temporal
lista_clientes: list[Cliente] = []

# =========================
# LISTAR CLIENTES
# =========================

@router_clientes.get("/clientes")
def listar_clientes():
    return {"clientes": lista_clientes}

# =========================
# CREAR CLIENTE
# =========================

@router_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):

    cliente_val = Cliente(
        id=len(lista_clientes) + 1,
        nombre=datos_cliente.nombre,
        edad=datos_cliente.edad,
        descripcion=datos_cliente.descripcion
    )

    lista_clientes.append(cliente_val)

    return cliente_val

# =========================
# OBTENER CLIENTE
# =========================

@router_clientes.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):

    for cliente in lista_clientes:

        if cliente.id == cliente_id:
            return cliente

    return {"mensaje": "Cliente no encontrado"}

# =========================
# EDITAR CLIENTE
# =========================

@router_clientes.put("/clientes/{id}", response_model=Cliente)
async def editar_cliente(id: int, datos_cliente: ClienteCrear):

    for i, obj_cliente in enumerate(lista_clientes):

        if obj_cliente.id == id:

            cliente_actualizado = Cliente(
                id=id,
                nombre=datos_cliente.nombre,
                edad=datos_cliente.edad,
                descripcion=datos_cliente.descripcion
            )

            lista_clientes[i] = cliente_actualizado

            return cliente_actualizado

    return {"mensaje": "Cliente no encontrado"}

# =========================
# ELIMINAR CLIENTE
# =========================

@router_clientes.delete("/clientes/{id}", response_model=Cliente)
def eliminar_cliente(id: int):

    for i, cliente in enumerate(lista_clientes):

        if cliente.id == id:

            eliminado = lista_clientes.pop(i)

            return eliminado

    return {"mensaje": "Cliente no encontrado"}