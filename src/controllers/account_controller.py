from services.account_service import AccountService

class AccountController:
    def __init__(self, service: AccountService):
        self.service = service

    def create_account(self, user_id: int, balance: float):
        return self.service.create_account(user_id, balance)

    def get_accounts(self):
        return self.service.get_accounts()