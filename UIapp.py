from DBConnection import DBConnection
from Email import Email
# from mainManager import animal_list, maxPlaces, new_animal_list
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class UIApp(App):
    new_animal_list = []
    animal_list = []
    maxPlaces = 7

    def __init__(self, nal, al, mp):
        App.__init__(self)
        self.new_animal_list = nal
        self.animal_list = al
        self.maxPlaces = mp

    def build(self):
        self.wrapper = BoxLayout(orientation='vertical', spacing=20)
        self.box = BoxLayout(orientation='horizontal', spacing=20)
        self.txt = TextInput(hint_text='Write here', size_hint=(.5, .1), pos_hint={'x': .65, 'y': .2})

        self.shelter_list = Label(text="Existing places: " + str(self.animal_list.append(self.new_animal_list)),
                                  size_hint=(.1, .15),
                                  pos_hint={'x': .5, 'y': .9})
        self.message = Label(text="You can add", size_hint=(.1, .15), pos_hint={'x': .5, 'y': .9})
        self.btnAdd = Button(text='Add to list', on_press=self.add, size_hint=(.1, .1), pos_hint={'x': .65, 'y': .2})
        self.btnDelete = Button(text='Delete from list', on_press=self.delete, size_hint=(.1, .1), pos_hint={'x': .65,
                                                                                                             'y': .2})
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
        if len(self.animal_list) < self.maxPlaces:
            self.message.text = "You can add"
            self.animal_list.append(self.txt.text)
            self.shelter_list.text = "Existing places: " + str(self.animal_list)
            self.txt.text = ''
            if self.maxPlaces - len(self.animal_list) < 2:
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
        if len(self.animal_list) > 0 and self.txt.text in self.animal_list:
            self.animal_list.remove(self.txt.text)
            self.shelter_list.text = "Existing places: " + str(self.animal_list)
        else:
            self.message.text = "Cannot find the animal to remove"

    def clearDB(self, event):
        del_tab = DBConnection()
        del_tab.name = "animals"
        del_tab.delete()
        self.animal_list.clear()
        self.shelter_list.text = "Existing places: " + str(self.animal_list)
