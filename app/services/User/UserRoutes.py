from fastapi import APIRouter, HTTPException
from app.services.User.UserController import create_user as create
from app.models.UserModel import SignUpSchema

router = APIRouter()


@router.post("/register")
async def create_user(user: SignUpSchema):
    """Create a new user"""
    try:
        return await create(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
