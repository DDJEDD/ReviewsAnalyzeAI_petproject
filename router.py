from fastapi import APIRouter, Depends
from Deps import get_Service, get_AIService
from Service import Service
from AI import AIService
from Validator import LanguageEnum, CreateReview, CreateProduct
router = APIRouter()


@router.post("/CreateProduct")
async def create_product(product: CreateProduct, Service = Depends(get_Service) ):
    return await Service.create_product(product.name, product.value)
@router.get("/GetProducts")
async def get_product(Service:Service = Depends(get_Service)):
    return await Service.get_products()
@router.post("/CreateReview")
async def create_review(CreateReview:CreateReview, Service:Service = Depends(get_Service)):
    return await Service.add_review(CreateReview)
@router.get("/get_reviews_by_id")
async def get_reviews_byid(id:int, Service:Service = Depends(get_Service)):
    return await Service.get_reviews_by_id(id)
@router.get("/getAiReview")
async def get_ai_review(id:int, country_code:LanguageEnum,  Service:Service = Depends(get_Service), AIService:AIService = Depends(get_AIService)):
    reviews = await Service.get_reviews_by_id(id)
    aireview = await AIService.send_request(reviews,country_code)
    return aireview