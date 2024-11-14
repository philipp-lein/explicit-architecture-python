from src.ApplicationCore.Port.Persistence.persistence_service_interface import PersistenceServiceInterface
from src.Infrastructure.Persistence.Django.entity.user import UserEntity


class DjangoPersistenceService(PersistenceServiceInterface):

    def upsert(self, entity) -> None:
        data = entity.to_dict()
        UserEntity(**data)