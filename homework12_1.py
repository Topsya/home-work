
from faker import Faker,Factory

fake = Factory.create('uk_UA')
AdresBook = []

def create_book (fake, AdresBook: list, n=10):
    for _ in range(n):
        user = {}
        user['name']= fake.name()
        user['phone '] = fake.phone_number()
        AdresBook.append(user)
    # print(AdresBook)
    return AdresBook


if __name__ == '__main__':
    create_book(fake,AdresBook, n=5)