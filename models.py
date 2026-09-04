from pydantic import BaseModel


class Producto(BaseModel):
    nombre: str
    stock: int
    precio: float

class Producto2(BaseModel):
    nombre: str
    stock: int
    precio: float
    id: int