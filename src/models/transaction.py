from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    
    account_id = Column(Integer, ForeignKey("accounts.id")) 
    
    amount = Column(Numeric(10, 2)) 
    
    transaction_type = Column(String(20)) 
    
    destination_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)