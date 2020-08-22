import sqlalchemy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, insert, select
from sqlalchemy.orm import sessionmaker
from Email import Email
from DBConnection import DBConnection

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


class ManagerApp(App):

    def build(self):
        self.wrapper = BoxLayout(orientation='vertical', spacing=20)
        self.box = BoxLayout(orientation='horizontal', spacing=20)
        self.txt = TextInput(hint_text='Write here', size_hint=(.5, .1), pos_hint={'x': .65, 'y': .2})

        self.shelter_list = Label(text="Existing places: " + str(animal_list.append(new_animal_list)), size_hint=(.1, .15),
                                  pos_hint={'x': .5, 'y': .9})
        self.message = Label(text="You can add", size_hint=(.1, .15), pos_hint={'x': .5, 'y': .9})
        self.btnAdd = Button(text='Add to list', on_press=self.add, size_hint=(.1, .1), pos_hint={'x': .65, 'y': .2})
        self.btnDelete = Button(text='Delete from list', on_press=self.delete, size_hint=(.1, .1),
                                pos_hint={'x': .65, 'y': .2})
        self.btnDeleteFromDb = Button(text='Clear database', on_press=self.clearDB, size_hint=(.1, .1),
                                      pos_hint={'x': .65, 'y': .2})
        self.wrapper.add_widget(self.shelter_list)
        self.wrapper.add_widget(self.message)

        self.box.add_widget(self.txt)
        self.box.add_widget(self.btnAdd)
        self.box.add_widget(self.btnDelete)
        self.box.add_widget(self.btnDeleteFromDb)
        self.wrapper.add_widget(self.box)
        return self.wrapper

    def add(self, event):
        if len(animal_list) < maxPlaces:
            self.message.text = "You can add"
            animal_list.append(self.txt.text)
            self.shelter_list.text = "Existing places: " + str(animal_list)
            self.txt.text = ''
            if maxPlaces - len(animal_list) < 2:
                self.message.text = "There is less than 2 places in the shelter"
                mail = Email()
                mail.receiver = "mzagula1992@gmail.com"
                mail.subject = "Alert! Check the shelter"
                mail.sender = "marta.testowe123@gmail.com"
                mail.message = "Please, check the state of the shelter. It is close to run out of places"

                mail.send_mail()
        else:
            self.message.text = "Shelter is full"

    def delete(self, event):
        if len(animal_list) > 0 and self.txt.text in animal_list:
            animal_list.remove(self.txt.text)
            self.shelter_list.text = "Existing places: " + str(animal_list)
        else:
            self.message.text = "Cannot find the animal to remove"

    def clearDB(self, event):
        del_tab = DBConnection()
        del_tab.name = "animals"
        del_tab.delete()
        animal_list.clear()
        self.shelter_list.text = "Existing places: " + str(animal_list)


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


ManagerApp().run()

# create df
col = ['animal_names']
vertical_list = df_from_list_to_column(animal_list)
print(vertical_list)
df = pd.DataFrame(vertical_list, columns=col)

# export to csv
df.to_csv('database.csv')

# export to database

engine = create_engine('postgresql://admin:admin@localhost:5432/ManagerApp')
metadata = MetaData(bind=engine)
animals = Table('animals', metadata, autoload=True)
conn = engine.connect()
metadata = MetaData()
Session = sessionmaker(bind=conn)
session = Session()

i = insert(animals)
for values in animal_list:
    i = i.values({"animal_name": values})
    session.execute(i)

session.commit()
