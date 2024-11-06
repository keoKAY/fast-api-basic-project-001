from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select 
from app.models import Product 
from app.schemas import ProductCreate 


async def create_prodcut(db: AsyncSession, product: ProductCreate): 
    db_product = Product(
        name=product.name, 
        description=product.description, 
        price=product.price
    )
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_products(db: AsyncSession, skip: int=0, limit: int = 10): 
    result = await db.execute(select(Product).offset(skip).limit(limit))
    return result.scalars().all()