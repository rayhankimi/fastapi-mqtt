from app.models.UserModel import LoginSchema, SignUpSchema
from app.middleware.firebase import create_new_user

from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException


async def create_user(user: SignUpSchema) -> JSONResponse:
    """Save user to database"""
    try:
        _user = create_new_user(user)
        return JSONResponse(status_code=201, content={"message": f"User created successfully for {_user.email}"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Error: User not created")
