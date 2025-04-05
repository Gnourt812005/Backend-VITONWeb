from sqlalchemy import Integer, String, Column, TIMESTAMP, Text
from app.core.database import Base 

class ImagePerson(Base):
    __tablename__ = "imageperson"
    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP)