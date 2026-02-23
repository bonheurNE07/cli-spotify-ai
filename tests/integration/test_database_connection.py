import pytest
from sqlalchemy import text
from app.infrastructure.database import engine

@pytest.mark.asyncio
async def test_database_connection() -> None:
    async with engine.begin() as connection:
        result = await connection.execute(text("SELECT 1"))
        value = result.scalar()
        
    assert value == 1
    