from fastapi import HTTPException, status

role_not_found = HTTPException(
    detail="Role with this id was not found",
    status_code=status.HTTP_404_NOT_FOUND,
)


role_exist = HTTPException(
    detail="Role with this name exist",
    status_code=status.HTTP_400_BAD_REQUEST,
)
