from fastapi import HTTPException, status

credentials_exception = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

user_active_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Inactive user",
    headers={"WWW-Authenticate": "Bearer"},
)


user_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found",
    headers={"WWW-Authenticate": "Bearer"},
)
