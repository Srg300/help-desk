from fastapi import HTTPException, status

role_not_found = HTTPException(
    detail="Role with this id was not found",
    status_code=status.HTTP_404_NOT_FOUND,
)
