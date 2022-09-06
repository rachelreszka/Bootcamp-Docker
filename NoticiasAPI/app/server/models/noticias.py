from datetime import datetime
from beanie import Document
from pydantic import BaseModel
from typing import Optional
 
 
class Noticias(Document):
    title: str
    desc: str
    link: str
    date: datetime 

class Settings:
    name = "noticias"
 
class Config:
    schema_extra = {
        "example": {
            "title": "Abdulazeez",
            "desc": "Abdulazeez",
            "link": "TestDriven TDD Course",
            "date": datetime.now()
        }
    }
 
 
class UpdateNoticias(BaseModel):
    title: Optional[str]
    desc: Optional[str]
    link: Optional[str]
    date: Optional[datetime]
 
class Config:
    schema_extra = {
        "example": {
            "title": "Abdulazeez Abdulazeez",
            "desc": "TestDriven TDD Course",
            "link": "Excellent course!",
            "date": datetime.now()
        }
    }