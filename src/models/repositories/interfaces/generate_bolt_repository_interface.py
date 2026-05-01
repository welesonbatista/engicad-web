from abc import ABC, abstractmethod


class BoltRepositoryInterface(ABC):

    @abstractmethod
    async def insert_bolt(self, bolt):
        pass

    @abstractmethod
    async def find_bolt_by_id(self, bolt_id):
        pass
