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
        # 1️⃣ Verifica se o usuário existe
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise AccountNotFoundError("Usuário não encontrado")

        # 2️⃣ Cria a conta
        account = Account(
            user_id=user_id,
            balance=balance
        )

        # Salva no banco
        return self.account_repository.create(account)

    def get_accounts(self):
        return self.account_repository.get_all()
