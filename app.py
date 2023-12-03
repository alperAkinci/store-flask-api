from flask import Flask, request
from db import stores, items
import uuid

# Creates flask app
app = Flask(__name__)

@app.get("/store")
def get_all_stores():
    return {"stores": list(stores.values())}

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return stores, 201

@app.post("/item")
def create_item():
    item_data = request.get_json()
    
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try: 
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try: 
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404