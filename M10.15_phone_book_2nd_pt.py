# Продолжаем расширять функциональность класса Contacts, на этом этапе мы добавим в класс метод get_contact_by_id. 
# Метод должен искать контакт по уникальному id в списке contacts и возвращать словарь из него с указанным ключом id. 
# Если словаря с указанным id в списке contacts не найдено, метод возвращает None

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for i in self.contacts:
            if i["id"] == id:
                return i
        return None

Con = Contacts()
Con.add_contacts("Anton","09345","email", True)
# print(Con.list_contacts())
Con.get_contact_by_id("1")
        