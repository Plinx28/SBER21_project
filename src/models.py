from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, TIMESTAMP, Text
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


class Calories(Base):
    __tablename__ = "calories"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    noted_at = Column(TIMESTAMP, default=datetime.utcnow)
    additional = Column(Text, nullable=True)

    user_id = mapped_column(Integer, ForeignKey("users.id"), unique=False, nullable=False)
    user = relationship("User", back_populates="calories")


class Pressure(Base):
    __tablename__ = "pressure"

    id = Column(Integer, primary_key=True)
    quantity_low = Column(Integer, nullable=False)
    quantity_high = Column(Integer, nullable=False)
    noted_at = Column(TIMESTAMP, default=datetime.utcnow)
    additional = Column(Text, nullable=True)

    user_id = mapped_column(Integer, ForeignKey("users.id"), unique=False, nullable=False)
    user = relationship("User", back_populates="pressure")
