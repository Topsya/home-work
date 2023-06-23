import json
from homework12_1 import AdresBook, create_book, fake

    

def json_file(AdresBook):
    with open('users_fail.json', 'w') as fh:
       json.dump(AdresBook,fh, indent=4, ensure_ascii=False) 
       print('AdresBook was creeate in json.')

def unpacked_file():
    with open('users_fail.json', 'r', encoding='utf-8') as readfail:
       unpacked_users = json.load(readfail) 
       print("AdresBook was unpacked.")
       return unpacked_users

def find_name_phone():
   unpacked_users = unpacked_file()
   vod_poisk = input('enter Name or Phone of abonent : ')
   # unpacked_users = unpacked_users.encod('utf-8')
   for i in unpacked_users:
        for value in i.values():
            if vod_poisk in value:
                print (f'  {i} ')
            else: 
                print ('no matches found in AdresBook')


if __name__ == '__main__':
#    create_book(fake,AdresBook, n=4)
#    json_file(AdresBook)
   unpacked_file()
   find_name_phone()
   