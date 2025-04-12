from sqlalchemy import Column, Integer, Text, UniqueConstraint
from app.core.database import Base 

class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(Text, nullable=False)

    __table_args__ = (
        UniqueConstraint("tag_name", name="tags_tag_name_key"),
    )