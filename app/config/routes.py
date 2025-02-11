from fastapi import APIRouter
from app.services.User.UserRoutes import router as user_router

main_router = APIRouter()

main_router.include_router(user_router, prefix="/user")
