from collections import UserDict
from datetime import datetime, timedelta
import json
import re

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass
    
class Phone(Field):
    def __init__(self,phone):
        self.phone = phone
    
    @property
    def phone(self):
            return self.phone

    @phone.setter
    def phone(self, phone):
            if re.findall(r'\d{11}', phone):
                self.phone = phone
            else:
                print ("Enter number '+' and 12 digits : ")

class Birthday(Field)   :
    def __init__(self, birthday):
        self.birthday = birthday
    @property
    def birthday(self):
            return self.birthday
        
    @birthday.setter
    def birthday(self, birthday):
            if datetime.strptime(birthday, '%m/%d/%Y'):
                self.birthday = birthday
            else:
                print ("Birthday format data mm/dd/yyyy : ")


        
class Record:
    phone = []

    def __init__(self, name, phone=None):
        self.name = name 
        self.phones = []
        if phone:
            self.phones.append(phone)
    
    def days_to_birthday(self, birthday=None):   
    #  ???????? ????????? ???? ?? ?????????? ??? ??????????
       if birthday:
        segodnya = datetime.now()
        one_year = timedelta(year=1)
        birthday_next = datetime(year= (segodnya.year + one_year), month= birthday.month, day = birthday.day)
        return birthday_next - segodnya
       

class AddressBook(UserDict):
 
    def add_record(self, record):
      self.data[record.name.value] = record

    # def iterator(self):
   
    def __iter__(self):
      return self
    def __next__(self):
       # ??????? ???????? ??????? ? AddressBook ?? ???? ???????? N
        N = 5 
        self.current = 0 

        if self.current  <= N:
            self.current  += 1
            return self.current 
        raise StopIteration

def json_file(AddressBook):
    with open('users_fail.json', 'w') as fh:
       json.dump(AddressBook,fh, indent=4, ensure_ascii=False) 
       print('AddressBook was creeate in json.')

def unpacked_file():
    with open('users_fail.json', 'r', encoding='utf-8') as readfail:
       unpacked_users = json.load(readfail) 
       print("AddressBook was unpacked.")
       return unpacked_users

def find_name_phone():
   unpacked_users = unpacked_file()
   vod_poisk = input('enter Name or Phone of abonent : ')
   # unpacked_users = unpacked_users.encod('utf-8')
   result = {}
   for i in unpacked_users:
        for value in i.values():
            if vod_poisk in value:
                result.update(i)
            # else: 
            #     print ('no matches found in AdresBook')
        
   if result == {}:
            print ('no matches found in AdresBook')
   print (result)    


if __name__ == "__main__":
    # name = Name ('Bill')
    # phone = Phone ('+123456789101')
    # rec = Record(name, phone)
    # ab = AddressBook()
    # ab.add_record(rec)
    # assert isinstance(ab['Bill'],Record)
    # assert isinstance(ab['Bill'].name,Name)
    # assert isinstance(ab['Bill'].phones,list)
    # assert isinstance(ab['Bill'].phones[0],Phone)
    # assert ab['Bill'].phones[0].value == '123'
     
    json_file(AddressBook)
    unpacked_file()
    find_name_phone()
print ('all ok')