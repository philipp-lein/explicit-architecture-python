from abc import ABC


class PersistenceServiceInterface(ABC):
    def upsert(self, entity) -> None:
        pass