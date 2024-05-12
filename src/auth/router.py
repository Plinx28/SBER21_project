from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.models import Role
from src.database import get_async_session
from src.auth.schemas import RoleCreate


router = APIRouter(
    prefix="/auth/role",
    tags=["Auth"]
)


@router.post("/")
async def add_role(new_role: RoleCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Role).values(**new_role.model_dump())
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "details": "Yod successfully added a new role"
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.get("/")
async def get_all_roles(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Role).order_by(Role.id.desc())
        response = await session.execute(query)
        await session.commit()
        return {
            "status": "success",
            "data": response.mappings().all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })