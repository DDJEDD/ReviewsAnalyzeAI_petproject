from fastapi import FastAPI
from router import router
from Exceptions.handler import productalreadyexists_hnd, productdoesntexists_hnd
from Exceptions.Service import ProductAlreadyExists, ProductDoesntExists
app = FastAPI(root_path="/auth",title="AIReview" )
app.include_router(router)

app.add_exception_handler(ProductAlreadyExists, productalreadyexists_hnd)
app.add_exception_handler(ProductDoesntExists, productdoesntexists_hnd)
@app.get("/")
def start():
    return {"status": "successful!"}