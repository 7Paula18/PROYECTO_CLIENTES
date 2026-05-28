from pydantic import BaseModel

# Datos que el usuario ENVÍA (NO incluye id)
class ClienteCrear(BaseModel):
    nombre: str
    edad: int
    descripcion: str | None = None


# Modelo que usa el sistema (incluye id)
class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int
    descripcion: str | None = None


class Factura(BaseModel):
    id: int
    fecha: str
    cliente: str
    valortotal: float


class Transacciones(BaseModel):
    id: int
    descripcion: str
    factura: list