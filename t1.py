from sqlalchemy import create_engine, MetaData, Table, insert, select
from sqlalchemy.orm import sessionmaker
import pandas as pd

engine = create_engine('postgresql://admin:admin@localhost:5432/ManagerApp')
connection = engine.connect()
metadata = MetaData()
animals = Table('animals', metadata, autoload=True, autoload_with=engine)
d = animals.delete()
connection.execute(d)