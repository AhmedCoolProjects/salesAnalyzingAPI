from pydantic import BaseModel, Field, EmailStr

class CustomerModel(BaseModel):
    gender: str = Field(...)
    age: int = Field(...)
    email: EmailStr = Field(...)
    satisfaction: int = Field(...)
