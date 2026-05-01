import uuid
from src.controllers.interfaces.generate_bolt import GenerateBoltInterface
from src.models.entities.bolt_entity import BoltEntity
from src.models.repositories.interfaces.generate_bolt_repository_interface import BoltRepositoryInterface


class GenerateBoltController(GenerateBoltInterface):

    def __init__(self, cad_service, bolt_repository: BoltRepositoryInterface):
        self.__cad_service = cad_service
        self.__bolt_repository = bolt_repository

    async def generate_bolt(self, data: dict) -> dict:
        self.__validate(data)

        file_path = await self.__cad_service.generate_bolt(
            diameter=data["diameter"],
            length=data["length"],
            head_height=data["head_height"],
            head_size=data["head_size"],
            hole=data["hole"]
        )

        bolt = BoltEntity(
            id=uuid.uuid4(),
            diameter=data["diameter"],
            length=data["length"],
            head_height=data["head_height"],
            head_size=data["head_size"],
            hole=data["hole"],
            file_path=file_path
        )

        await self.__bolt_repository.insert_bolt(bolt)

        return {
            "data": {
                "file": file_path
            }
        }

    async def find_bolt_by_id(self, bolt_id) -> dict:
        bolt = await self.__bolt_repository.find_bolt_by_id(bolt_id)

        if not bolt:
            raise Exception("Bolt not found")

        return {
            "data": {
                "id": str(bolt.id),
                "diameter": bolt.diameter,
                "length": bolt.length,
                "head_height": bolt.head_height,
                "head_size": bolt.head_size,
                "hole": bolt.hole,
                "file_path": bolt.file_path
            }
        }

    def __validate(self, data: dict):
        if data.get("diameter", 0) <= 0:
            raise Exception("Diameter must be greater than 0")

        if data.get("length", 0) <= 0:
            raise Exception("Length must be greater than 0")

        if data.get("head_height", 0) <= 0:
            raise Exception("Head height must be greater than 0")

        if data.get("head_size", 0) <= data.get("diameter", 0):
            raise Exception("Head size must be greater than diameter")

        if data.get("hole", 0) <= 0:
            raise Exception("Hole must be greater than 0")

        if data.get("hole", 0) >= data.get("diameter", 0):
            raise Exception("Hole must be smaller than diameter")
