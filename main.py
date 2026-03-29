from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router
from Exceptions.handler import productalreadyexists_hnd, productdoesntexists_hnd
from Exceptions.Service import ProductAlreadyExists, ProductDoesntExists
from fastapi.staticfiles import StaticFiles
app = FastAPI(root_path="/auth",title="AIReview" )
app.include_router(router)
app.mount("/", StaticFiles(directory="front", html=True), name="front")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(ProductAlreadyExists, productalreadyexists_hnd)
app.add_exception_handler(ProductDoesntExists, productdoesntexists_hnd)
@app.get("/")
def start():
    return {"status": "successful!"}