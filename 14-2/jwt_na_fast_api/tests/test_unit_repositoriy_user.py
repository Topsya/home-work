import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from jwt_na_fast_api.schemas import UserModel
from jwt_na_fast_api.database.models import User
from jwt_na_fast_api.repository.users import get_user_by_email, create_user, update_token, confirmed_email, update_avatar 

# get_user_by_email , create_user, update_token, confirmed_email,  update_avatar 

class TestUsersRepository(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.session = MagicMock(spec=Session)

    async def test_get_user_by_email(self):
        email = "test_mail@example.com"
        user = User(id=1,  email=email)
        self.session.query().filter_by().first.return_value = user

        result = await get_user_by_email(email=email, db=self.session)
        self.assertEqual(result, user)

    async def test_get_user_by_email_nonexistent(self):
        user_email = "non_existent_mail@example.com"
        self.session.query().filter_by().first.return_value = None

        result = await get_user_by_email(email=user_email, db=self.session)
        self.assertIsNone(result)

    async def test_create_user(self):
                       
        user_data = UserModel (username="nnnnnn", email="test@example.com", password="password12")
        new_user = User(id=1, email=user_data.email)
        self.session.add.return_value = None
        self.session.commit.return_value = None
        self.session.refresh.return_value = None

        result = await create_user(body=user_data, db=self.session)
        self.assertEqual(result.email, new_user.email)



    async def test_update_token(self):
        user = User(id=1,  email="test_mail@example.com")
        token = "new_refresh_token"
        self.session.commit.return_value = None
        self.session.refresh.return_value = None

        await update_token(user=user, token=token, db=self.session)
        self.assertEqual(user.refresh_token, token)

    async def test_confirmed_email(self):
        user_email = "test_mail@example.com"
        user = User(id=1,  email=user_email, confirmed=True)
        self.session.commit.return_value = None
        self.session.refresh.return_value = None

        await confirmed_email(email=user_email, db=self.session)
        self.assertTrue(user.confirmed)

    async def test_update_avatar(self):
        user_email = "test_mail@example.com"
        avatar_url = "https://fake.com/avatar.png"
        self.session.commit.return_value = None
        self.session.refresh.return_value = None

        updated_user = await update_avatar(email=user_email,  url=avatar_url, db=self.session)
        self.assertEqual(updated_user.url, avatar_url)


if __name__ == '__main__':
    unittest.main()