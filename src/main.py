from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from src.statistics.pressure.router import router as router_pressure
from src.statistics.calories.router import router as router_calories
from src.pages.router import router as router_pages

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserCreate, UserRead
from src.config import SECRET_KEY


app = FastAPI(title="Medecine SBER service",
              description="Service for medecine organization 'Центр индустрии здоровья'",
              version="MVP")

app.mount("/static", StaticFiles(directory="src/static"), name="static")

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=("GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"),
    allow_headers=("Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"),
)

if SECRET_KEY is None:
    raise "Missing SECRET_KEY"
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_pressure)
app.include_router(router_calories)
app.include_router(router_pages)
