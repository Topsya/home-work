from libgravatar import Gravatar
from sqlalchemy.orm import Session
from jwt_na_fast_api.database.models import User
from jwt_na_fast_api.schemas import UserModel

async def get_user_by_email(email: str, db: Session) -> User:
    """
    The get_user_by_email function return  user by email  from the database.

    :param email: The email of the contact to retrieve.
    :type email: str
    :param db: The database session.
    :type db: Session
    :return: The user with the email, or None if it does not exist.
    :rtype: User | None
    """
    return db.query(User).filter(User.email == email).first()

async def create_user(body: UserModel, db: Session) -> User:
    """
    Creates a new User.

    :param body: UserModel:  the type of data that is expected to be passed into the function.
    :type body: UserModel
    :param db: The database session.
    :type db: Session
    :return: The newly created User .
    :rtype: User 
    """
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)
    new_user = User(**body.dict(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    """
    Updates a single user  token.

    :param user: The user  to update.
    :type user: User
   
    :param token: The user to update token.
    :type token: str
    :param db: The database session.
    :type db: Session
    :return: The updated User token, or None if it does not exist.
    :rtype: User | None
    """
    user.refresh_token = token
    db.commit()

async def confirmed_email(email: str, db: Session) -> None:
    """
    The confirmed_email function confirmed User by email .

    :param email: The email of the User ho mast be confirmed .
    :type email: str
    :param db: The database session.
    :type db: Session
    :return: The user with the email, or None if it does not confirmed .
    :rtype: User | None
    """

    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()

async def update_avatar(email, url: str, db: Session) -> User:
    """
    Updates a single user avatar.

    :param user: The user  to update.
    :type user: User
   
    :param avatar: The str linck to update avatar.
    :type avatar: str
    :param db: The database session.
    :type db: Session
    :return: The updated User , or None if it does not exist.
    :rtype: User | None
    """
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user


