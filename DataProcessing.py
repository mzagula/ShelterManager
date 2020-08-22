import pandas as pd

class DataProcessing():

    def df_from_df_to_list(df):
        list_df = []
        for j in df:
            print(j)
            list_df.append(j)
        return list_df

    def df_table_to_list(animals_data,animal_name):
        df = pd.DataFrame(animals_data)
        if not df.empty:
            df.columns = animals_data[0].keys()
            animal_list = DataProcessing.df_from_df_to_list(df[animal_name])
        else:
            animal_list=[]

        return animal_list

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
