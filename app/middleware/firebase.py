import firebase_admin
from firebase_admin import credentials, auth
from fastapi.exceptions import HTTPException
from fastapi import Security
from fastapi.security import HTTPBearer
from firebase_admin.auth import verify_id_token

from app.models.UserModel import SignUpSchema

cred = credentials.Certificate("firebaseConfig.json")
firebase_admin.initialize_app(cred)

security = HTTPBearer()


def create_new_user(user: SignUpSchema):
    """Create new user in firebase"""
    try:
        if user:
            _user = auth.create_user(
                email=user.email,
                email_verified=False,
                password=user.password,
                display_name=user.username,
            )
            return _user
        else:
            HTTPException(status_code=400, detail="Client Error: Invalid user data")
    except Exception as e:
        raise ValueError(f"Error: {e}")


def verify_firebase_token(token: str = Security(security)):
    """
    """
    try:
        decoded_token = verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
