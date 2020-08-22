import pandas as pd
from DBConnection import DBConnection
from UIApp import UIApp
from DataProcessing import DataProcessing

animal_list = []
maxPlaces = 7

# read db state
connection = DBConnection()
animals_data = connection.select("animals", "")
animal_list = DataProcessing.df_table_to_list(animals_data, "animal_name")

UIApp(animal_list, maxPlaces).run()

# col = ['animal_names']
# vertical_list = DataProcessing.df_from_list_to_column(animal_list)
# df = pd.DataFrame(vertical_list, columns=col)

