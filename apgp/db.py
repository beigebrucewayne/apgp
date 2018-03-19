import asyncio
import asyncpg

from .config import _read_config

class DB:

    def __init__(self, query: str):
        self.query: str = query
        self.dsn: str = _read_config()

    async def run(self) -> list:
        conn = await asyncpg.connect(self.dsn)
        values = await conn.fetch(self.query)
        await conn.close()
        return values
