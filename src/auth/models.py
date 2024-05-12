from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column

from fastapi_users.db import SQLAlchemyBaseUserTable

from src import Base


class Role(Base):
    __tablename__ = "roles"

    id = mapped_column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(String, nullable=True)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    pressure = relationship("Pressure", back_populates="user", cascade="all, delete-orphan")
    calories = relationship("Calories", back_populates="user", cascade="all, delete-orphan")

    role_id = mapped_column(Integer, ForeignKey("roles.id"))
