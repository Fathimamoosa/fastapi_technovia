from sqlalchemy import Column, Integer, String
from app.database import Base


class UserForms(Base):
    __tablename__ = "userData"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    message = Column(String(200), nullable=False)