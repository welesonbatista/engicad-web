from sqlalchemy import select
from src.models.entities.bolt_entity import BoltEntity
from src.core.database_connection_handler import DBConnectionHandler
from src.models.repositories.interfaces.generate_bolt_repository_interface import BoltRepositoryInterface



class BoltRepository(BoltRepositoryInterface):

    async def insert_bolt(self, bolt: BoltEntity) -> BoltEntity:
        async with DBConnectionHandler() as db:
            assert db.session is not None
            db.session.add(bolt)
            await db.session.commit()
        return bolt

    async def find_bolt_by_id(self, bolt_id):
        async with DBConnectionHandler() as db:
            assert db.session is not None
            query = select(BoltEntity).where(BoltEntity.id == bolt_id)
            result = await db.session.execute(query)
            return result.scalar_one_or_none()
