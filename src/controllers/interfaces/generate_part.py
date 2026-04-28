from abc import ABC, abstractmethod

class GeneratePartInterface(ABC):
    @abstractmethod
    async def generate_part(self, data_part: dict) -> dict:
        pass

    @abstractmethod
    async def find_part_by_id(self, part_id: int) -> dict:
        pass