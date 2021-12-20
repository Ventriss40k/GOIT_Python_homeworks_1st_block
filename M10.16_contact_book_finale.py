# Завершаем функциональность класса Contacts. 
# На этом этапе мы добавим в класс метод remove_contacts. Метод должен удалять контакт по уникальному id в списке contacts. 
# Если словаря с указанным id в списке contacts не найдено, метод никаких действий над списком contacts не производит.

# Примечание: для правильного прохождения теста не создавайте экземпляр класса в коде.
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
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        for i in self.contacts:
            if i["id"] == id: self.contacts.remove(i)
        

        
        
            