from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

#  AQUÍ VALIDAMOS QUE SE ACEPTEN SOLO CARACTERES ESPECIFICOS EN LOS CAMPOS
class Order(BaseModel):
    cliente: str
    producto: str
    cantidad: int

#Este modelo es lo que devuelve es sistema
class OrderResponse(BaseModel):
    id: int
    cliente: str
    producto: str
    cantidad: int
    estado: str


# "Base de datos" temporal
orders_db = []

#Es un contador automático de IDs y sirve para darle un número único a cada pedido
order_id_counter = 1

@app.get("/")
def home():
    return {"message": "API funcionando 🚀"}

# Crear pedido
@app.post("/orders")
def create_order(order: Order):
    global order_id_counter

    new_order = {
        "id": order_id_counter,
        "cliente": order.cliente,
        "producto": order.producto,
        "cantidad": order.cantidad,
        "estado": "pendiente"
    }

    orders_db.append(new_order)
    order_id_counter += 1

    return new_order

# Ver pedidos
@app.get("/orders")
def get_orders():
    return {
        "orders": orders_db
    }