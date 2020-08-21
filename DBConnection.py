from sqlalchemy import create_engine, MetaData, Table, insert, select
from sqlalchemy.orm import sessionmaker


class DBConnection:
    def __init__(self):
        self.engine = create_engine('postgresql://admin:admin@localhost:5432/ManagerApp')
        self.connection = self.engine.connect()
        self.metadata = MetaData()

    # arguments: String table, String where
    # return: df
    def select(self, table, where):
        table = Table(table, self.metadata, autoload=True, autoload_with=self.engine)
        query = select([table])

        ResultProxy = self.connection.execute(query)
        ResultSet = ResultProxy.fetchall()

        return ResultSet





    # animals = Table('animals', metadata, autoload=True, autoload_with=engine)
