from sqlalchemy.orm import Session
from repositories.transaction_repository import TransactionRepository
from repositories.account_repository import AccountRepository
from models.transaction import Transaction
from utils.validators import validate_positive_value
from utils.errors import AccountNotFoundError, InsufficientBalanceError
from utils.enum import TransactionType


class TransactionService:
    def __init__(
        self,
        db: Session,
        transaction_repository: TransactionRepository,
        account_repository: AccountRepository
    ):
        self.db = db
        self.transaction_repository = transaction_repository
        self.account_repository = account_repository

    def create_transaction(
        self,
        account_id: int,
        amount: float,
        transaction_type: TransactionType,
        destination_account_id: int | None = None
    ):
        try:
            account = self.account_repository.get_by_id(account_id)
            if not account:
                raise AccountNotFoundError("Conta não encontrada")

            validate_positive_value(amount)

            if transaction_type in [TransactionType.WITHDRAW, TransactionType.TRANSFER]:
                if account.balance < amount:
                    raise InsufficientBalanceError("Saldo insuficiente")

            destination = None
            if transaction_type == TransactionType.TRANSFER:
                if not destination_account_id:
                    raise AccountNotFoundError("Conta de destino obrigatória")

                destination = self.account_repository.get_by_id(destination_account_id)
                if not destination:
                    raise AccountNotFoundError("Conta de destino não encontrada")

            if transaction_type == TransactionType.DEPOSIT:
                account.balance += amount

            elif transaction_type == TransactionType.WITHDRAW:
                account.balance -= amount

            elif transaction_type == TransactionType.TRANSFER:
                account.balance -= amount
                destination.balance += amount
                self.db.add(destination)

            self.db.add(account)

            transaction = Transaction(
                account_id=account.id,
                amount=amount,
                transaction_type=transaction_type.value,
                destination_account_id=destination.id if destination else None
            )

            self.db.add(transaction)

            self.db.commit()

            self.db.refresh(transaction)
            return transaction

        except Exception:
            self.db.rollback()
            raise

    def get_transactions(self, account_id: int):
        return self.transaction_repository.get_by_account(account_id)
