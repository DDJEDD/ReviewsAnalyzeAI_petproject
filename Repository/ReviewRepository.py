from sqlalchemy import select
from sqlalchemy.orm import selectinload

from Database.models import Review

class ReviewRepository:
    def __init__(self,session):
        self.session = session
    async def create_review(self,username:str,text:str, product_id:int):
        new_review = Review(
            username=username,
            text=text,
            product_id=product_id
        )
        self.session.add(new_review)
        return new_review

    async def get_All_reviews_from_one_product(self, product_id: int):
        stmt = select(Review).options(selectinload(Review.product)).where(Review.product_id == product_id)
        res = await self.session.execute(stmt)
        reviews = res.scalars().all()
        return reviews