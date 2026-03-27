from fastapi import APIRouter, Depends, Query
from Deps import get_Service, get_AIService
from Service import Service
from AI import AIService
from Validator import LanguageEnum, CreateReview
router = APIRouter()


@router.post("/CreateProduct")
async def createproduct(name:str, Service:Service = Depends(get_Service) ):
    return await Service.create_product(name)

@router.post("/CreateReview")
async def createreview(CreateReview:CreateReview, Service:Service = Depends(get_Service)):
    return await Service.add_review(CreateReview)
@router.get("/get_reviews_by_id")
async def getreviewsbyid(id:int, Service:Service = Depends(get_Service)):
    return await Service.get_reviews_by_id(id)
@router.get("/getAiReview")
async def getaireview(id:int, country_code:LanguageEnum,  Service:Service = Depends(get_Service), AIService:AIService = Depends(get_AIService)):
    reviews = await Service.get_reviews_by_id(id)
    aireview = await AIService.send_request(reviews,country_code)
    return aireview