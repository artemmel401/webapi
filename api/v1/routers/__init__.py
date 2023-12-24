from fastapi import APIRouter

from api.v1.routers.authors import router as authors_router
from api.v1.routers.genres import router as genres_router
from api.v1.routers.books import router as books_router

router = APIRouter(prefix='/v1')

router.include_router(authors_router)
router.include_router(genres_router)
router.include_router(books_router)
