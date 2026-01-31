from repositories.account_repository import AccountRepository
from repositories.user_repository import UserRepository
from models.account import Account
from utils.errors import AccountNotFoundError

class AccountService:
    def __init__(
        self,
        account_repository: AccountRepository,
        user_repository: UserRepository
    ):
        self.account_repository = account_repository
        self.user_repository = user_repository

    def create_account(self, user_id: int, balance: float):

        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise AccountNotFoundError("Usuário não encontrado")

        account = Account(
            user_id=user_id,
            balance=balance
        )
        return self.account_repository.create(account)

    def get_accounts(self):
        return self.account_repository.get_all()
