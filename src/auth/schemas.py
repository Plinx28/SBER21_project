from pydantic import EmailStr
from fastapi_users import schemas


class UserBase(schemas.BaseUser):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class UserRead(UserBase):
    email: EmailStr
