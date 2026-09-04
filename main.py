from base import get_connection, initDb
from fastapi import FastAPI
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


app = FastAPI()


@app.on_event("startup")
def startup():
    print("iniciamos db")
    initDb()


@app.post("/agregar")
def postProduct(producto: Producto):
    conexion = (get_connection())  
    conexion.execute("INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)",
    (producto.nombre, producto.stock, producto.precio),
    )
    conexion.commit()
    conexion.close()
    return f"guardado en la db {producto}"

@app.get("/leer_productos")
def getproductos():
    conexion = get_connection()
    res = conexion.execute("SELECT * FROM productos").fetchall()
    return [dict(item) for item in res]

@app.delete("/eliminar_productos/{id}")
def deletproductos(id: int):
    conexion = get_connection()
    conexion.execute("DELETE FROM productos WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    return f"se elimino {id}"

#actualizar
@app.put("/actualizarproducto/{id}")
def actualizarproducto(producto: Producto2):
    conexion = get_connection()
    nuevonombre = producto.nombre 
    nuevostock = producto.stock
    nuevoprecio = producto.precio 
    id = producto.id
    conexion.execute("UPDATE productos SET nombre = ?, stock = ?, precio = ?  WHERE id = ?", (nuevonombre, nuevostock, nuevoprecio, id))
    conexion.commit()
    conexion.close()
    return f"se actualizo {id}"
    
@app.get("/")
def read_root():
    return "hola"


