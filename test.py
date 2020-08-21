from DBConnection import DBConnection
import pandas as pd

connection = DBConnection()
animals = connection.select("animals","")

df = pd.DataFrame(animals)
print(animals[0].keys())