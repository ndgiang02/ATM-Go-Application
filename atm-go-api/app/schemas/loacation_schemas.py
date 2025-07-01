from pydantic import BaseModel
from typing import Optional

class LocationBase(BaseModel):
    link: Optional[str]
    title: str
    category: Optional[str]
    address: str
    open_hours: Optional[str]
    website: Optional[str]
    phone: Optional[str]
    review_rating: Optional[float]
    latitude: Optional[float]
    longitude: Optional[float]
    descriptions: Optional[str]
    owner: Optional[str]
    bank_code: Optional[str]
    type: Optional[str]

class LocationCreate(LocationBase):
    pass

class LocationOut(LocationBase):
    id: int

    class Config:
        orm_mode = True