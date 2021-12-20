# Есть список, каждый элемент которого это словарь с контактами пользователя следующего вида:
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     }
# Словарь содержит, имя пользователя name, его email, телефонный номер phone и свойство favorite — избранный контакт или нет.
# Разработайте две функции для сериализации и десериализации списка контактов, с помощью пакета pickle и хранения полученных данных в бинарном файле.
# Первая функция write_contacts_to_file принимает два параметра: filename имя файла, contacts список контактов. Она сохраняет указанный список в файл используя метод dump пакета pickle.
# Вторая функция read_contacts_from_file читает и возвращает указанный список contacts из файла filename используя метод load пакета pickle.
import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename,"wb") as fh:
        pickle.dump(contacts,fh)
    
def read_contacts_from_file(filename):
    with open(filename,"rb") as fh:
        return pickle.load(fh)
    
        
contacts = "Test"
# write_contacts_to_file("pickle.bin",contacts)
