from sqlalchemy.orm import Session
from models.account import Account

class AccountRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, account: Account):
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account

    def get_all(self):
        return self.db.query(Account).all()

    def get_by_id(self, account_id: int):
        return self.db.query(Account).filter(Account.id == account_id).first()

    def update(self, account: Account):
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account