from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    
    # Qual conta está fazendo isso?
    account_id = Column(Integer, ForeignKey("accounts.id")) 
    
    # O valor da grana
    amount = Column(Numeric(10, 2)) 
    
    # O "tipo": aqui você vai salvar as palavras 'DEPOSIT', 'WITHDRAW' ou 'TRANSFER'
    transaction_type = Column(String(20)) 
    
    # Opcional: Para onde foi o dinheiro (se for transferência)
    destination_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)