from pandas import DataFrame
import asyncio

from .db import DB


class Query:

    def __init__(self, query: str):
        self.query = query
        self._loop = asyncio.get_event_loop()

    def execute(self) -> DataFrame:
        db = DB(self.query)
        values = self._loop.run_until_complete(db.run())
        return correct_columns(values)

    def close(self):
        self._loop.close()


def correct_columns(vals: list) -> DataFrame:
    columns = [i for i in vals[0].keys()]
    data = DataFrame(vals)
    data.columns = columns
    return data
