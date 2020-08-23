from sqlalchemy import create_engine, MetaData, Table, insert, select
from sqlalchemy.orm import sessionmaker


class DBConnection:
    name = ""

    def __init__(self):
        self.engine = create_engine('postgresql://admin:admin@localhost:5432/ManagerApp')
        self.connection = self.engine.connect()
        self.metadata = MetaData()

    def select(self, table, where):
        table = Table(table, self.metadata, autoload=True, autoload_with=self.engine)
        query = select([table])

        ResultProxy = self.connection.execute(query)
        ResultSet = ResultProxy.fetchall()

        return ResultSet

    def delete(self):
        table = Table(self.name, self.metadata, autoload=True, autoload_with=self.engine)
        query = table.delete()
        self.connection.execute(query)

    def insert(self, insert_value, column):
        metadata = MetaData(bind=self.engine)
        table = Table(self.name, metadata, autoload=True)
        Session = sessionmaker(bind=self.connection)
        session = Session()
        i = insert(table).values({column: insert_value})
        session.execute(i)

        session.commit()

    def delete_from(self, where_value):
        table = Table(self.name, self.metadata, autoload=True, autoload_with=self.engine)
        d = table.delete().where(table.c.animal_name == where_value)
        self.connection.execute(d)
        # query = table.filter_by(animal_name=where_value).delete()
        # self.connection.execute(query)
