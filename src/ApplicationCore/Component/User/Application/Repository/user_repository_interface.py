from abc import abstractmethod, ABC # Abstract Base Classes


from src.ApplicationCore.Component.User.Domain.user import User
from src.ApplicationCore.Port.Persistence.persistence_service_interface import PersistenceServiceInterface


class UserRepositoryInterface(ABC):
    def __init__(self, persistence_service: PersistenceServiceInterface):
        self.persistence_service = persistence_service

    @abstractmethod
    def add(self, user: User):
        """adds a new user to the repository"""
        pass