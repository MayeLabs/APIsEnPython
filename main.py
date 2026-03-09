import requests
from fastapi import FastAPI

app = FastAPI() # Instancia de la api

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
def read_items(q: str=None):
    if q:
        return {'items':['Item 1', 'Item 2', 'Item 3'], "query": q} # "query": q → incluye el valor del parámetro que llegó por la URL
    return {"items": ["Item 1", "Item 2", "Item 3"]}

# item_id => Parametro de ruta 
# q => Parametro opcional
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query":q}

# Método POST
@app.post("/items/")
def create_item(item: dict):
    return {"item": item}

# Método PUT
@app.put("/items/{item_id}")
def update_item(item_id:int, item: dict):
    return {"item_id":item_id, "updated_item": item}

# Método DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
