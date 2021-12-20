# Как вы уже поняли, для класса Contacts создание поверхностной копии экземпляра класса не увенчается успехом, 
# так как мы имеем атрибут contacts, который является списком экземпляров объектов класса Person,
#  а значит все они будут переданы по ссылке. Поэтому необходимо использовать глубокое копирование методом deepcopy из пакета copy

# Для класса Contacts реализуйте функцию copy_class_contacts. В качестве параметра она принимает экземпляр класса Contacts,
#  и возвращает глубокую копию объекта с помощью функции deepcopy из пакета copy.
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

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
        self.__dict__ = value
        self.is_unpacking = True


def copy_class_contacts(contacts):
  return copy.deepcopy(contacts)