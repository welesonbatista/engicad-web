from src.controllers.interfaces.generate_part import GeneratePartInterface
from src.models.repositories.part_repository import PartRepositoryInterface
from src.models.entities.part_entity import PartEntity
import uuid


class GeneratePartController(GeneratePartInterface):

    def __init__(self, cad_service, part_repository: PartRepositoryInterface):
        self.__cad_service = cad_service
        self.part_repository = part_repository

    async def generate_part(self, data_part: dict) -> dict:
        self.__validate_generate_part(data_part)

        file_path = await self.__generate_cad(data_part)
        part = self.__build_entity(data_part, file_path)

        await self.part_repository.insert_part(part)

        return {
            "data": {
                "file": file_path
            }
        }

    async def find_part_by_id(self, part_id: int) -> dict:
        part = await self.part_repository.find_part_by_id(part_id)

        if not part:
            raise Exception("Part not found")

        return {
            "data": {
                "id": part.id,
                "diameter": part.diameter,
                "length": part.length,
                "hole_diameter": part.hole_diameter,
                "file_path": part.file_path
            }
        }

    def __validate_generate_part(self, data_part: dict):
        if data_part.get("diameter", 0) <= 0:
            raise Exception("Diameter must be greater than 0")

        if data_part.get("length", 0) <= 0:
            raise Exception("Invalid length.")

        if data_part.get("hole_diameter", 0) >= data_part.get("diameter"):
            raise Exception(
                "Hole diameter must be smaller than the part diameter."
            )

    async def __generate_cad(self, data_part: dict) -> str:
        return await self.__cad_service.generate(
            diameter=data_part["diameter"],
            length=data_part["length"],
            hole=data_part["hole_diameter"]
        )

    def __build_entity(self, data_part: dict, file_path: str) -> PartEntity:
        return PartEntity(
            id=uuid.uuid4(),
            diameter=data_part["diameter"],
            length=data_part["length"],
            hole_diameter=data_part["hole_diameter"],
            file_path=file_path
        )
