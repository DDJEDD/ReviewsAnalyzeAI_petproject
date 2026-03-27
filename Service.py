from Repository import ProductRepository, ReviewRepository
from  Exceptions.Service import ProductAlreadyExists, ProductDoesntExists
class Service:
    def __init__(self, session, ProductRepository: ProductRepository, ReviewRepository: ReviewRepository ):
        self.session = session
        self.ProductDirectory = ProductRepository
        self.ReviewRepository = ReviewRepository
    async def create_product(self, name):
        async with self.session.begin():
            if await self.ProductDirectory.CheckProduct(name):
                raise ProductAlreadyExists()
            await self.ProductDirectory.createProduct(name)
        return {"Status":"Successful"}
    async def add_review(self,username:str, text:str,product_id:int):
        async with self.session.begin():
            if not await self.ProductDirectory.CheckProduct_by_id(product_id):
                raise ProductDoesntExists()
            await self.ReviewRepository.create_review(username,text,product_id)
        return {"Status":"Successful"}

    async def get_reviews_by_id(self, id: int):
        reviews = await self.ReviewRepository.get_All_reviews_from_one_product(id)
        return [
            f"товар: {r.product.name}|отзыв: {r.text} "
            for r in reviews
        ]