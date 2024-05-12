from pydantic import BaseModel


class PressureBase(BaseModel):
    quantity_low: int
    quantity_high: int
    additional: str


class CreatePressure(PressureBase):
    pass
