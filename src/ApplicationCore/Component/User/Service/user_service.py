from src.ApplicationCore.Component.User.Application.Repository.user_repository_interface import UserRepositoryInterface
from src.ApplicationCore.Component.User.Domain.user import User


class UserService(object):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, username) -> User:
        user = User(username)
        self.user_repository.add(user)
        return user
