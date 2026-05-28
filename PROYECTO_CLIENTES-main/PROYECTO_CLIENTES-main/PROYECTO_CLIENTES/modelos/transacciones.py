from pydantic import BaseModel

class Transaccion(BaseModel):
    id: int
    descripcion: str
    factura: int