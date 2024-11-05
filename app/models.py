from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base 

class SeasonalFlavor(Base):
    __tablename__ = 'seasonal_flavors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)  


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    quantity = Column(Integer)  
    
class CustomerFeedback(Base):
    __tablename__ = "customer_feedback"

    id = Column(Integer, primary_key=True, index=True)
    suggestion = Column(String)
    allergy_concern = Column(String)
    handled = Column(Boolean, default=False)
