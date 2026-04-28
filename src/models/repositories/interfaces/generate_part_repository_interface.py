from abc import ABC, abstractmethod

class PartRepositoryInterface(ABC):

    @abstractmethod
    async def insert_part(self, part: dict):
        pass

    @abstractmethod
    async def find_part_by_id(self, part_id: int):
        pass