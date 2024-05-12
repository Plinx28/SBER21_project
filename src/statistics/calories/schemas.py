from pydantic import BaseModel


class CaloriesBase(BaseModel):
    quantity: int
    additional: str
    user_id: int


class CreateCalories(CaloriesBase):
    pass
