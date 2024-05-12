from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from src.statistics.pressure.router import get_all_pressure
from src.statistics.calories.router import get_all_calories


router = APIRouter(
    prefix="/page",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/home")
def get_home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/statistics")
def get_statistics_page(request: Request,
                        statistics={
                            "pressure": Depends(get_all_pressure),
                            "calories": Depends(get_all_calories)
                        }
                        ):
    return templates.TemplateResponse("statistics.html", {"request": request, "statistics": statistics})
