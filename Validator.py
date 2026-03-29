from pydantic import BaseModel, Field
from enum import Enum
class LanguageEnum(str, Enum):
    EN = "English"
    RU = "Russian"
    UK = "Ukrainian"
    ES = "Spanish"
    FR = "French"
    DE = "German"
    IT = "Italian"
    PL = "Polish"
    PT = "Portuguese"
    ZH = "Chinese"
    JA = "Japanese"
    KO = "Korean"
class CreateReview(BaseModel):
    username: str
    product_id: int
    text: str
class CreateProduct(BaseModel):
    name:str
    value:str = Field(pattern=r'^\d+(\.\d+)?[€$£]$')
