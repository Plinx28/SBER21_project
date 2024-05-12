from fastapi import APIRouter, Depends

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from src.database import get_async_session

from src.statistics.calories.schemas import CreateCalories
from src.models import Calories

router = APIRouter(
    prefix="/calories",
    tags=["Calories"]
)


@router.get("/")
async def get_all_calories(current_user_id: int, session: Session = Depends(get_async_session)):
    query = select(Calories).where(user_id=current_user_id).order_by(Calories.noted_at).limit(25)
    calories_history = await session.execute(query).all()
    return {"calories": calories_history}


@router.post("/")
async def add_calories(new_calories: CreateCalories,  session: Session = Depends(get_async_session)):
    stmt = insert(Calories).values(**new_calories.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
