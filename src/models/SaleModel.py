from pydantic import BaseModel,Field
from src.models.PyObjectId import PyObjectId
from src.models.ItemModel import ItemModel
from src.models.CustomerModel import CustomerModel
from bson import ObjectId
from datetime import datetime

class SaleModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    items: list[ItemModel] = Field(default_factory=list)
    customer: CustomerModel = Field(default_factory=CustomerModel)
    couponUsed: bool = Field(...)
    purchaseMethod: str = Field(...)
    saleDate: datetime = Field(...)
    storeLocation: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId:str}
        # schema_extra = {
        #     "example": {

        #     }
        # }