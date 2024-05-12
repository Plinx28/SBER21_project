from fastapi import APIRouter, Depends
from src.auth.base_config import fastapi_users

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from src.database import get_async_session

from src.statistics.calories.schemas import CreateCalories
from src.models import Calories
from src.auth.base_config import get_enabled_backends

router = APIRouter(
    prefix="/calories",
    tags=["Calories"]
)

current_active_user = fastapi_users.current_user(active=True, get_enabled_backends=get_enabled_backends)


@router.get("/")
async def get_all_calories(session: Session = Depends(get_async_session)):
    current_user_id = 1  # TODO заглушка ID
    query = select(Calories).where(user_id=current_user_id).order_by(Calories.noted_at).limit(25)
    calories_history = await session.execute(query).all()
    return {"calories": calories_history}


@router.post("/")
async def add_calories(new_calories: CreateCalories,
                       session: Session = Depends(get_async_session),
                       current_user=Depends(current_active_user)):
    new_calories.user_id = current_user.id
    stmt = insert(Calories).values(**new_calories.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
