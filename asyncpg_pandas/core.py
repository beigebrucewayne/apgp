import abc
import asyncpg
import pandas


class AsyncDatabase:

    @abc.abstractmethod
    async def connection(self):

    @abc.abstractmethod
    async def get_coroutine(self, coroutine, sql_query, *args,
                            connection=None, timeout=None,
                            close_connection=True):

    async def query(self, sql_query, *args, connection=None, timeout=None,
                    close_connection=True):
        return await self.get_coroutine('fetch', sql_query, *args,
                                        connection=connection, timeout=timeout,
                                        close_connection=close_connection)
