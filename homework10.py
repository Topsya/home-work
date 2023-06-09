from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass
    # def __init__(self, value):
    #     self.value = value
class Phone(Field):
    def __init__(self,value):  
        self.value = value
       
class Record:
   # phone = []
    def __init__(self, name, phone=None):
        self.name = name 
        self.phones = []

        if phone:
            self.phones.append(phone)

class AddressBook(UserDict):
 
    def add_record(self, record):
      self.data[record.name.value] = record
                    # Як ключі використовується значення Record.name.value 

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)

    assert isinstance(ab['Bill'].phones[0], Phone)
    
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')