from sqlalchemy import Column, Integer, String, Float, Text
from app.db.database import Base

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    title = Column(String)
    category = Column(String)
    address = Column(String)
    open_hours = Column(Text)
    website = Column(String)
    phone = Column(String)
    review_rating = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    descriptions = Column(Text)
    owner = Column(Text)
    bank_code = Column(String)
    type = Column(String)