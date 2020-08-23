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

