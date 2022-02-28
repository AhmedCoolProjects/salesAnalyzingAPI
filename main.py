from typing import Optional
from fastapi import FastAPI
from src.models.SaleModel import SaleModel
from src.utils.connectDB import db
app = FastAPI()





@app.get("/")
def read_root():
    return {"Hello": "thanks GOD"}
    
@app.get("/items/{item_id}")
def read_item(item_id:int, q: Optional[str] = None):
    return {"item_id":item_id,"q":q}

@app.get("/sales",response_description="List of all sales",
        response_model=list[SaleModel]
        )
async def list_sales():
    sales = await db["sales"].find().to_list(length=1)
    return sales