from fastapi.responses import JSONResponse
from fastapi import Request

def exception_handler(status_code:int, detail:str):
    async def handler(request: Request, exc: Exception):
        return JSONResponse(status_code=status_code, content={"detail": detail})
    return handler

productalreadyexists_hnd = exception_handler(409, "Product Already Exists")
productdoesntexists_hnd = exception_handler(409, "Product Doesnt Exists")


