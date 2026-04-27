import pytest
from src.core.database_connection_handler import DBConnectionHandler


@pytest.mark.asyncio
async def test_db_connection():
    async with DBConnectionHandler() as db_handler:
        assert db_handler.session is not None

