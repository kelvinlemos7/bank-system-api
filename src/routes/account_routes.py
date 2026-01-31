from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.account_controller import AccountController
from services.account_service import AccountService
from repositories.account_repository import AccountRepository
from repositories.user_repository import UserRepository
from schemas.account_schema import AccountCreate, AccountResponse
from database import get_db

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post("/", response_model=AccountResponse)
def create_account_route(
    account: AccountCreate,
    db: Session = Depends(get_db)
):
    account_repository = AccountRepository(db)
    user_repository = UserRepository(db)
    account_service = AccountService(account_repository, user_repository)
    account_controller = AccountController(account_service)

    return account_controller.create_account(
        account.user_id,
        account.balance
    )

@router.get("/", response_model=List[AccountResponse])
def get_accounts_route(db: Session = Depends(get_db)):
    account_repository = AccountRepository(db)
    user_repository = UserRepository(db)
    account_service = AccountService(account_repository, user_repository)
    account_controller = AccountController(account_service)

    return account_controller.get_accounts()
