from base import get_connection, initDb
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlite3 import Connection
from productosmanager import productosmanager2

productosmana = productosmanager2()


class Producto(BaseModel):
    nombre: str
    stock: int
    precio: float

class Producto2(BaseModel):
    nombre: str
    stock: int
    precio: float
    id: int


app = FastAPI()


@app.on_event("startup")
def startup():
    print("iniciamos db")
    initDb()


@app.post("/agregar")
def postProduct(producto: Producto, conexion: Connection = Depends(get_connection)):
    return productosmana.agregarProducto(producto, conexion)

@app.get("/leer_productos")
def getproductos(conexion: Connection = Depends(get_connection)):
    return productosmana.leerProducto(conexion)

@app.delete("/eliminar_productos/{id}")
def deletproductos(id: int, conexion: Connection = Depends(get_connection)):
    return productosmana.eliminar(id, conexion)

#actualizar
@app.put("/actualizarproducto/{id}")
def actualizarproducto(producto: Producto2, conexion: Connection = Depends(get_connection)):
    return productosmana.actualizar(producto, conexion) 
    
@app.get("/")
def read_root():
    return "hola"


