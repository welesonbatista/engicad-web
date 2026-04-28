from typing import Any, Dict
from sqlalchemy import insert, select
from src.models.entities.part_entity import PartEntity
from src.core.database_connection_handler import DBConnectionHandler
from .interfaces.generate_part_repository_interface import PartRepositoryInterface

class PartRepository(PartRepositoryInterface):

    async def insert_part(self, part: Dict[str, Any]):
        async with DBConnectionHandler() as db:
            assert db.session is not None

            query = insert(PartEntity).values(**part)
            await db.session.execute(query)
            await db.session.commit()

        return part

    async def find_part_by_id(self, part_id: int):
        async with DBConnectionHandler() as db:
            assert db.session is not None

            query = select(PartEntity).where(PartEntity.id == part_id)
            result = await db.session.execute(query)
            return result.scalar_one_or_none()
