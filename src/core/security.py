from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from settings import AuthSettings, get_settings

_settings = get_settings(AuthSettings)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(subject: str, expires_delta: timedelta | None) -> str:
    if expires_delta:
        expire = datetime.now(tz=timezone.utc) + expires_delta
    else:
        expire = datetime.now(tz=timezone.utc) + timedelta(
            minutes=_settings.jwt_access_lifetime,
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    return jwt.encode(to_encode, _settings.secret_key, algorithm=_settings.secret_key)  # type: ignore[no-any-return]


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
