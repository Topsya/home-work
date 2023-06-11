from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass
    # def __init__(self, value):
    #     self.value = value
class Phone(Field):
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
       
class Record:
    phone = []

    def __init__(self, name, phone):
        self.name = name 

        if phone:
            self.phones = []
            self.phones.append(phone)

class AddressBook(UserDict):
 
    def add_record(self, record):
      self.data[record.name.value] = record
                    # Як ключі використовується значення Record.name.value 

