import json
from homework12_1 import AdresBook, create_book, fake

    

def json_file(AdresBook):
    with open('users_fail.json', 'w') as fh:
       json.dump(AdresBook,fh, indent=4, ensure_ascii=False) 
       print('AdresBook was creeate in json.')

def unpacked_file():
    with open('users_fail.json') as readfail:
       unpacked_users = json.load(readfail) 
       print("AdresBook was unpacked.")
       return unpacked_users




if __name__ == '__main__':
    create_book(fake,AdresBook, n=4)
    json_file(AdresBook)