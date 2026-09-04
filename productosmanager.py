from models import Producto
from models import Producto2
import sqlite3

class productosmanager2:
    def __init__(self):
        pass

    def agregarProducto(self, producto: Producto, conexion: sqlite3.Connection):
        conexion.execute("INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)",
        (producto.nombre, producto.stock, producto.precio),
        )
        return "estudiante agrego"

    def leerProducto(self, conexion: sqlite3.Connection):
        res = conexion.execute("SELECT * FROM productos").fetchall()
        return [dict(item) for item in res]

    def eliminar(self, id, conexion: sqlite3.Connection):
        conexion.execute("DELETE FROM productos WHERE id = ?", (id,))
        return f"se elimino {id}"

    def actualizar(self, producto: Producto2, conexion: sqlite3.Connection):
        nuevonombre = producto.nombre 
        nuevostock = producto.stock
        nuevoprecio = producto.precio 
        id = producto.id
        conexion.execute("UPDATE productos SET nombre = ?, stock = ?, precio = ?  WHERE id = ?", (nuevonombre, nuevostock, nuevoprecio, id))
