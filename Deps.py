from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from Database.database import get_async_session
from Service import Service
from Repository.ProductRepository import ProductRepository
from Repository.ReviewRepository import ReviewRepository
from AI import AIService
from config import API_URL, BEARER_TOKEN
from httpx import AsyncClient
async def get_Service(session: AsyncSession = Depends(get_async_session)):
    return Service(session,  ProductRepository(session), ReviewRepository(session))
async def get_AIService():
    return AIService(AsyncClient(timeout=None), BEARER_TOKEN, API_URL)