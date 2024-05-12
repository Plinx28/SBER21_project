from pydantic import BaseModel


class PressureBase(BaseModel):
    quantity_low: int
    quantity_high: int
    description: str


class CreatePressure(PressureBase):
    owner: int
