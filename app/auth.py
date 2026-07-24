from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

from app.core.config import settings

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
    token,
    settings.SECRET_KEY,
    algorithms=[settings.ALGORITHM]
)

        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )