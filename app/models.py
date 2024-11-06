import uuid 
from sqlalchemy import Column, String , Float 
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.ext.declarative import declarative_base

Base =    declarative_base()
class Product(Base): 
    __tablename__="products"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name= Column(String , index=True)
    description=Column(String)
    price= Column(Float)