from fastapi import FastAPI
from firebase import db

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    doc_ref = db.collection("items").document(item_id)
    doc = doc_ref.get()
    return {"data": doc.to_dict()}