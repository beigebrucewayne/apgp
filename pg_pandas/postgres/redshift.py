import psycopg2
import pandas as pd
import pandas.io.sql as psql

from .exceptions import RedshiftReadError, RedshiftWriteError
from .columns import check_columns


class Redshift:
    """
    Connecting To AWS Redshift Cluster

    All configuration details are read in from `config.yaml` file.

    Example:

        # Connect to Redshift
        redshift, s3 = connect()

        # Query Redshift
        df = redshift.to_pandas('SELECT * FROM table_name')

        # Run SQL Query
        redshift.exec_commit('SELECT * FROM table_name')
    """
    def __init__(self, dbname: str, host: str, port: int, user: str, **kwargs):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user

        allowed_key = set(['password'])
        self.__dict__.update((key, False) for key in allowed_key)
        self.__dict__.update((key, value) for key, value in kwargs.items()
                             if key in allowed_key)

        self._cursor = _connect_to_redshift(self.dbname, self.host, self.port,
                                            self.user, password=self.password)

    def to_pandas(self, sql_query, dates_to_parse=None, chunks=None):
        """
        sql_query:  str
            Query to send to Redshift.

        dates_to_parse : list or dict, default: None
            List of column names to parse as dates.
            Dict of {column_name: format string} where format string is
            strftime compatible in case of parsing string times, or is one of
            (D, s, ns, ms, us) in case of parsing integer timestamps.


        chunks : int, default None
            If specified, return an iterator where chunksize is the number
            of rows to include in each chunk.
        """
        try:
            data = psql.read_sql(sql_query, connect, parse_dates=dates_to_parse,
                                 chunksize=chunks)
            data = data.infer_objects()  # Should provide back better dtypes
            return data
        except RedshiftReadError:
            raise RedshiftReadError('Unable to read data from Redshift.')

    def exec_commit(self, sql_query):
        # Standard SQL Query via psycopg2
        self._cursor.execute(sql_query)
        connect.commit()


def _connect_to_redshift(dbname, host, port, user, **kwargs):
    # Shouldn't be invoked directly
    # Instead, the function will be invoked during
    # Redshift class initialization
    global connect
    connect = psycopg2.connect(dbname=dbname, host=host, port=port, user=user,
                               **kwargs)
