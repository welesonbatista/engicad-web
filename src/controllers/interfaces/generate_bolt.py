from abc import ABC, abstractmethod


class GenerateBoltInterface(ABC):

    @abstractmethod
    async def generate_bolt(self, data: dict) -> dict:
        pass

    @abstractmethod
    async def find_bolt_by_id(self, bolt_id) -> dict:
        pass
