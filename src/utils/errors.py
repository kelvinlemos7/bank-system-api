class UserNotFoundError(Exception):
    pass

class AccountNotFoundError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class BusinessError (Exception):
    pass

class DuplicateUserError (Exception):
    pass

class InvalidTransactionError (Exception):
    pass

class InvalidEmailError (Exception):
    pass

class InvalidNameError (Exception):
    pass

class InvalidValueError (Exception):
    pass