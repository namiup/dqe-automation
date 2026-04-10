
import psycopg2

class PostgresConnectorContextManager:
    def __init__(self, db_host: str, db_name: str, db_user: str, db_password: str):
        # init
        pass

    def __enter__(self):
        # create conn
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        # close con
        pass

    def get_data_sql(self, sql):
        # exec query, result = pandas df
        pass


