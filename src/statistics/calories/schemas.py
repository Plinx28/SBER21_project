from pydantic import BaseModel


class CaloriesBase(BaseModel):
    quantity: int
    description: str


class CreateCalories(CaloriesBase):
    owner: int
