import pandas as pd
from DBConnection import DBConnection
from UIApp import UIApp

new_animal_list = []
animal_list = []
maxPlaces = 7

def df_from_df_to_list(df):
    list_df = []
    for j in df:
        print(j)
        list_df.append(j)
    return list_df


# read db state
connection = DBConnection()
animals_data = connection.select("animals", "")

df = pd.DataFrame(animals_data)
if not df.empty:
    df.columns = animals_data[0].keys()
    animal_list = df_from_df_to_list(df['animal_name'])

def df_from_list_to_column(list_to_col):
    vertical_data = []
    if len(list_to_col) > 0:
        for i in list_to_col:
            row = [i]
            vertical_data.append(row)
    return vertical_data


def df_from_column_to_list(vertical_data):
    list = []
    for i in vertical_data:
        list.append(i[0])
    return list


UIApp(new_animal_list,animal_list,maxPlaces).run()

# create df
col = ['animal_names']
vertical_list = df_from_list_to_column(animal_list)
print(vertical_list)
df = pd.DataFrame(vertical_list, columns=col)

# export to csv
#df.to_csv('database.csv')

# export to database
animal_ins = DBConnection()
animal_ins.name = "animals"
animal_ins.insert(animal_list,"animal_name")

