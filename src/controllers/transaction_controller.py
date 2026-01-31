from services.transaction_service import TransactionService

class TransactionController:
    def __init__(self, service: TransactionService):
        self.service = service

    def create_transaction(self, account_id, amount, transaction_type, destination_account_id=None):
        return self.service.create_transaction(
            account_id,
            amount,
            transaction_type,
            destination_account_id
        )
    
    
