from sqlalchemy import Select

from Database.models import Product
class ProductRepository:
    def __init__(self ,session):
        self.session = session
    async def createProduct(self, name:str):
        new_product = Product(
            name=name
        )
        self.session.add(new_product)
        return new_product
    async def CheckProduct(self, name:str):
        stmt = Select(Product).where(Product.name == name)
        res = await self.session.execute(stmt)
        product = res.scalar_one_or_none()
        return product is not None
    async def CheckProduct_by_id(self, id:int):
        stmt = Select(Product).where(Product.id == id)
        res = await self.session.execute(stmt)
        product = res.scalar_one_or_none()
        return product is not None