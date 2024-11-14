from src.ApplicationCore.Component.User.Application.Repository.user_repository_interface import UserRepositoryInterface
from src.ApplicationCore.Component.User.Domain.user import User


class UserRepository(UserRepositoryInterface):
    def add(self, user: User):
        self.persistence_service.upsert(user)