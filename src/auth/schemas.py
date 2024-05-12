from pydantic import EmailStr, BaseModel
from fastapi_users import schemas


class UserBase(schemas.BaseUser):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class UserRead(UserBase):
    email: EmailStr


class RoleCreate(BaseModel):
    id: int
    name: str
    permissions: str
