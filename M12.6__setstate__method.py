# Продолжаем расширять пример из предыдущей задачи. Добавьте в класс Contacts атрибут is_unpacking, 
# по умолчанию он должен иметь значение False. Реализуйте магический метод __setstate__ для класса Contacts. 
# При распаковке экземпляра класса метод должен изменять значение атрибута is_unpacking на значение True. 
# Таким образом это свойство будет определять, что экземпляр класса получен в результате распаковки.
# Пример работы кода:

# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# person_from_file = persons.read_from_file()
# print(persons.is_unpacking)  # False
# print(person_from_file.is_unpacking)  # True
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking  = False
        

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__["is_unpacking"] = True
        
        