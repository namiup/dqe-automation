import psycopg2

class PostgresConnectorContextManager:
    def __init__(self, db_host: str, db_port: str, db_name: str, db_user: str, db_password: str):
        # init
        pass

    def __enter__(self):
        # create conn
        conn = psycopg2.connect(
        dbname="db_name",
        user="db_user",
        password="db_password",
        host="db_host"
        )

    def __exit__(self, exc_type, exc_value, exc_tb):
        # close conn
        cur.close()
        conn.close()

    def get_data_sql(self, sql):
        # exec query, result = pandas df
        df = pd.read_sql_query(sql, conn)
        return df

mycon = PostgresConnectorContextManager('localhost', '5434', 'mydatabase', 'myuser', 'mypassword')
print(mycon.get_data_sql("select 1"))
