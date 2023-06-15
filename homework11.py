from collections import UserDict
from datetime import datetime, timedelta
import re

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass
    
class Phone(Field):
    def __init__(self,phone):
        self.phone = phone

class Birthday(Field)   :
    def __init__(self, birthday):
        self.birthday = birthday

@property
def phone(self):
        return self.phone

@phone.setter
def phone(self, phone):
        if re.findall(r"\+\d{12}",phone):
            self.phone = phone
        else:
            raise ValueError("Enter number '+' and 12 digits : ")
    
@property
def birthday(self):
        return self.birthday
    
@birthday.setter
def birthday(self, birthday):
        if datetime.strptime(birthday, '%m/%d/%Y'):
            self.birthday = birthday
        else:
            raise ValueError("Birthday format data mm/dd/yyyy : ")
        
class Record:
    phone = []

    def __init__(self, name, phone=None):
        self.name = name 
        self.phones = []
        if phone:
            self.phones.append(phone)
    
    def days_to_birthday(self, birthday=None):   
    #  повертає кількість днів до наступного дня народження
       if birthday:
        segodnya = datetime.now()
        one_year = timedelta(year=1)
        birthday_next = datetime(year= (segodnya.year + one_year), month= birthday.month, day = birthday.day)
        return birthday_next - segodnya
       

class AddressBook(UserDict):
 
    def add_record(self, record):
      self.data[record.name.value] = record
                    

# if __name__ == "__main__":
#     name = Name ('Bill')
#     phone = Phone ('+123456789101')
#     rec = Record(name, phone)
#     ab = AddressBook()
#     ab.add_record(rec)
#     assert isinstance(ab['Bill'],Record)
#     assert isinstance(ab['Bill'].name,Name)
#     assert isinstance(ab['Bill'].phones,list)
#     assert isinstance(ab['Bill'].phones[0],Phone)
#     assert ab['Bill'].phones[0].value == '123'
# print ('all ok')