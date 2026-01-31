from pydantic import BaseModel

class AccountBase(BaseModel):
    user_id: int
    balance: float

class AccountCreate(AccountBase):
    pass

class AccountResponse(AccountBase):
    id: int

    class Config:
        from_attributes = True  
