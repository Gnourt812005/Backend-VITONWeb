from sqlalchemy import Column, String, Boolean, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID 
from app.core.database import Base
from uuid import uuid4

class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="users_pkey"),
        UniqueConstraint("username", name="users_username_uniq"),
    )