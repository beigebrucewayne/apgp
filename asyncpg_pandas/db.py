import abc
import asyncpg


class ABCDatabase:
    @abc.abstractmethod
    async def get_connection(self):

    @abc.abstractmethod
    async def call_coroutine(self, coroutine_name, sql_query, *args,
                             connection=None, timeout=None,
                             close_connection=True):

    async def query(self, sql_query, *args, connection=connection, timeout=timeout,
                    close_connection=close_connection):
        return await self.call_coroutine('fetch', sql_query, *args,
                                         connection=connection,
                                         timeout=timeout,
                                         close_connection=close_connection)


class Database(ABCDatabase):

    def __init__(self, dsn, **kwargs):
        self.dsn = dsn
        self.kwargs = kwargs

    async def get_connection(self):
        return await asyncpg.connect(self.dsn, self.kwargs)

    async def call_coroutine(self, coroutine_name, sql_query, *args,
                             connection=None, timeout=None, close_connection=True):
        conn = connection or await self.get_connection()
        get_coroutine = getattr(conn, coroutine_name)
        try:
            return await get_coroutine(sql_query, *args, timeout=timeout)
        finally:
            if close_connection:
                await conn.close()
