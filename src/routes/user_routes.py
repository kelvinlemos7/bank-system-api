from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.user_controller import UserController
from services.user_service import UserService
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate, UserResponse
from database import get_db

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    repository = UserRepository(db)
    service = UserService(repository)
    controller = UserController(service)

    return controller.create_user(
        name=user.name,
        email=user.email
    )


@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)
    controller = UserController(service)

    return controller.get_users()
