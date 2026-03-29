
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    value = Column(String, nullable=False)
    reviews = relationship("Review", back_populates="product")


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    text = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="reviews")
