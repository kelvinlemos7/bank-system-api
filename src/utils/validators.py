from utils.errors import AccountNotFoundError, UserNotFoundError, DuplicateUserError, InsufficientBalanceError, BusinessError, InvalidTransactionError, InvalidEmailError, InvalidNameError, InvalidValueError

def validate_positive_value(value: float):
    if value <= 0:
        raise InsufficientBalanceError("Valor deve ser maior que zero")
    
def validate_email(email: str):
    if "@" not in email:
        raise InvalidEmailError("Email inválido")
    
def validate_name(name: str):
    if name.strip() == "":
        raise InvalidNameError("Nome inválido")
