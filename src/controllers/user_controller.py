from services.user_service import UserService

class UserController:
    def __init__(self, service: UserService):
        self.service = service

    def create_user(self, name: str, email: str):
        return self.service.create_user(name, email)

    def get_users(self):
        return self.service.get_users()