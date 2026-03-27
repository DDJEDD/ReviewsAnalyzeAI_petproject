from fastapi import APIRouter, Depends
from Deps import get_Service, get_AIService
from Service import Service
from AI import AIService
router = APIRouter()


@router.post("/CreateProduct")
async def createproduct(name:str, Service:Service = Depends(get_Service) ):
    return await Service.create_product(name)

@router.post("/CreateReview")
async def createreview(username:str,id:int,text:str, Service:Service = Depends(get_Service)):
    return await Service.add_review(username=username,product_id=id,text=text)
@router.get("/get_reviews_by_id")
async def getreviewsbyid(id:int, Service:Service = Depends(get_Service)):
    return await Service.get_reviews_by_id(id)
@router.post("/get")
async def getaireview(id:int,  Service:Service = Depends(get_Service), AIService:AIService = Depends(get_AIService)):
    reviews = await Service.get_reviews_by_id(id)
    aireview = await AIService.send_request(reviews)
    return aireview