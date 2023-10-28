import unittest
from unittest.mock import MagicMock
from datetime import date, timedelta

from sqlalchemy.orm import Session

from jwt_na_fast_api.repository.contacts_book import read_contact, read_contacts, create_contact, update_contact, remove_contact, read_contact_days_to_birthday
from jwt_na_fast_api.database.models import Contact, User
from jwt_na_fast_api.schemas import    ContactMoedels, ContactsBase


class TestContact(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    async def test_read_contacts(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter().offset().limit().all.return_value = contacts
        result = await read_contacts(  user=self.user, db=self.session)
        self.assertEqual(result, contacts)

    async def test_read_contact(self):
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await read_contact(contact_id=1, user=self.user, db=self.session)
        self.assertEqual(result, contact)

    async def test_if_read_contact_not_found(self):
        self.session.query().filter().first.return_value = None
        result = await read_contact(contact_id=1, user=self.user, db=self.session)
        self.assertIsNone(result)

    async def test_create_contact(self):
        body = ContactMoedels( name = 'John', surname = 'Street',  email = 'asdd@ddddd.net', fonenamber = '+380505555555', birthday = '12.12.2000', user_id = self.user.id )
        
        result = await create_contact(body=body, db=self.session)
        self.assertEqual(result.name, body.name)
        self.assertEqual(result.surname, body.surname)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.fonenamber, body.fonenamber)
        self.assertEqual(result.user_id, self.user.id)
        self.assertTrue(hasattr(result, "id"))
#   

    async def test_remove_contact_found(self):
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await remove_contact(contact_id=1, user=self.user, db=self.session)
        self.assertEqual(result, contact)

    async def test_remove_contact_not_found(self):
        self.session.query().filter().first.return_value = None
        result = await remove_contact(contact_id=1, user=self.user, db=self.session)
        self.assertIsNone(result)

    async def test_update_contact_found(self):
        body = ContactMoedels( name = 'John', surname = 'Street',  email = 'asdd@ddddd.net', fonenamber = '+380505555555', birthday = '12.12.2000', user_id = self.user.id )

        cont  = Contact( name = 'Anton', surname = 'BBBBBBB',  email = 'dsds@dsdsdsds.net', fonenamber = '+380506666666', birthday = '11.11.2000', user_id = self.user.id )

        self.session.query().filter_by().first.return_value = cont
        self.session.commit.return_value = None
        result = await update_contact(body=body, contact_id=cont.id, db=self.session)
    
        self.assertEqual(result.name, body.name)
        self.assertEqual(result.surname, body.surname)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.fonenamber, body.fonenamber)
        self.assertEqual(result.user_id, self.user.id)
        self.assertTrue(hasattr(result, "id"))

    async def test_update_contact_not_found(self):
        body = ContactMoedels(name = 'John', surname = 'Street',  email = 'asdd@ddddd.net', fonenamber = '+380505555555', birthday = '12.12.2000', user_id = self.user.id)
        self.session.query().filter().first.return_value = None
        self.session.commit.return_value = None
        result = await update_contact(contact_id=1, body=body, user=self.user, db=self.session)
        self.assertIsNone(result)
    
    
    async def test_read_contact_days_to_birthday(self):
        contact_1 = Contact(birthday=date.today() + timedelta(days=5))
        contact_2 = Contact(birthday=date.today() + timedelta(days=10))

        self.session.query().filter_by().all.return_value = [contact_1, contact_2]
        days = 14
        result = await read_contact_days_to_birthday(days=days, user=self.user, db=self.session)

        self.assertIn(contact_1, result)
        self.assertIn(contact_2, result)

    async def test_read_contact_days_to_birthday_not_found(self):
        contact1 = Contact(birthday=date.today() - timedelta(days=25))
        expected_result = None
        self.session.query().filter_by().all.return_value = [contact1]
        days = 14
        result = await read_contact_days_to_birthday(days=days, user=self.user, db=self.session)

        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()
