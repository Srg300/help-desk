from fastapi import HTTPException, status

user_not_found = HTTPException(
    detail="User with this id was not found",
    status_code=status.HTTP_404_NOT_FOUND,
)


user_exist = HTTPException(
    detail="User with this email exist",
    status_code=status.HTTP_400_BAD_REQUEST,
)
