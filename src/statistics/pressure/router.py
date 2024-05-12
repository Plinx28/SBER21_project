from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_async_session

router = APIRouter(
    prefix="/pressure",
    tags=["Pressure"]
)


@router.get("/")
def get_all_pressure(session: Session = Depends(get_async_session)):
    return {"pressure": "graphic and info. Everything is good or not at all"}


@router.post("/")
def add_pressure(session: Session = Depends(get_async_session)):
    return {"pressure": "Pressure note was posted successfully"}
