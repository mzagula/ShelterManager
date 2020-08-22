import pandas as pd
from DBConnection import DBConnection
from UIApp import UIApp
from DataProcessing import DataProcessing

new_animal_list = []
animal_list = []
maxPlaces = 7

# read db state
connection = DBConnection()
animals_data = connection.select("animals", "")

df = pd.DataFrame(animals_data)
if not df.empty:
    df.columns = animals_data[0].keys()
    animal_list = DataProcessing.df_from_df_to_list(df['animal_name'])

UIApp(new_animal_list, animal_list, maxPlaces).run()

# create df
col = ['animal_names']
vertical_list = DataProcessing.df_from_list_to_column(animal_list)
print(vertical_list)
df = pd.DataFrame(vertical_list, columns=col)

# export to csv
# df.to_csv('database.csv')

# export to database
animal_ins = DBConnection()
animal_ins.name = "animals"
animal_ins.insert(animal_list, "animal_name")
