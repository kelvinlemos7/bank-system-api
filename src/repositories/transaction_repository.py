from sqlalchemy.orm import Session
from models.transaction import Transaction

class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, transactions: Transaction):
        self.db.add(transactions)
        self.db.commit()
        self.db.refresh(transactions)
        return transactions
    
    def get_all(self):
        return self.db.query(Transaction).all()
    
    def get_by_account(self, account_id: int):
         return (
            self.db
            .query(Transaction)
            .filter(Transaction.account_id == account_id)
            .all()
        )
    

    