from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app import models, schemas, crud 
from app.db import engine, get_db


app=FastAPI(title="Product API ")

# create database tables on startup 
@app.on_event("startup")
async def startup(): 
    async with engine.begin() as conn: 
        await conn.run_sync(models.Base.metadata.create_all)
@app.post("/products", response_model=schemas.Product)
async def create_product (product: schemas.ProductCreate, db: AsyncSession = Depends(get_db)): 
    return await crud.create_prodcut(db=db, product=product)


@app.get("/products/", response_model=List[schemas.Product])
async def read_product(skip: int = 0, limit: int=10, db: AsyncSession=Depends(get_db)): 
    products = await crud.get_products(db, skip=skip, limit= limit)
    return products