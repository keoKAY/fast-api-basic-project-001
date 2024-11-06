from pydantic import BaseModel, UUID4
class ProductBase(BaseModel): 
    name: str 
    description: str 
    price: float 

class ProductCreate(ProductBase): 
    pass # means 

class Product(ProductBase):
    id: UUID4
    class Config: 
            orm_mod=True 