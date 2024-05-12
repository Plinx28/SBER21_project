from sqlalchemy import Column, Integer, TIMESTAMP, Text, ForeignKey
from sqlalchemy.orm import relationship, mapped_column

from datetime import datetime
from src import Base


class Pressure(Base):
    __tablename__ = "pressure"

    id = Column(Integer, primary_key=True)
    quantity_low = Column(Integer, nullable=False)
    quantity_high = Column(Integer, nullable=False)
    noted_at = Column(TIMESTAMP, default=datetime.utcnow)
    additional = Column(Text, nullable=True)

    user_id = mapped_column(Integer, ForeignKey("users.id"), unique=False, nullable=False)
    user = relationship("User", back_populates="pressure")
