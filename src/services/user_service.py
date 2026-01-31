from repositories.user_repository import UserRepository
from models.user import User
from utils.errors import DuplicateUserError
from utils.validators import validate_name, validate_email

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, name: str, email: str):
        validate_name(name)
        validate_email(email)

        existing_user = self.repository.get_by_email(email)
        if existing_user:
            raise DuplicateUserError ("Email já cadastrado")

        user = User(name=name, email=email)
        return self.repository.create(user)

    def get_users(self):
        return self.repository.get_all()
    
    
        
