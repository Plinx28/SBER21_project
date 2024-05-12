from fastapi import Depends

from fastapi_users.db import SQLAlchemyUserDatabase

# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.models import User
from src.database import get_async_session


def get_user_db(session: Session = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
