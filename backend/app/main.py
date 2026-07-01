from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.feed import router as feed_router
from app.api.routes.health import router as health_router
from app.api.routes.convert import router as convert_router

from app.storage.repository import feed_repository

app = FastAPI()


@app.on_event("startup")
def startup():
    feed_repository.create_table()


# ==============================
# CORS
# ==============================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==============================
# Routes
# ==============================

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

app.include_router(
    feed_router,
    prefix="/feed",
    tags=["Feed"]
)

app.include_router(
    convert_router,
    prefix="/convert",
    tags=["Convert"]
)