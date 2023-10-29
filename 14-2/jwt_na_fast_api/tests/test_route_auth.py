from unittest.mock import MagicMock

from jwt_na_fast_api.database.models import User

def test_create_user(client, user, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("jwt_na_fast_api.routes.auth.send_email", mock_send_email)
    response = client.post(
        "/api/auth/signup",
        json=user,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["user"]["email"] == user.get("email")
    assert "id" in data["user"]
#Під час тестів ми не хочемо надсилати лист користувачу для верифікації email. Для цього необхідно виконати мок функції send_email. 
# Ми будемо використовувати MagicMock, який автоматично створить мок-об'єкт з усіма необхідними методами та атрибутами, включно з await, який використовується у функції send_email. 
# Для підміни функції send_email ми використовуємо monkeypatch.

# INFO
# Цей механізм в pytest дозволяє замінити об'єкт у процесі виконання тестів. Об'єкт monkeypatch використовують для заміни значення змінної оточення, функції або класу на фіктивні значення під 
# час виконання тестів.

# Метод monkeypatch.setattr підміняє виклик функції send_email з модуля src.routes.auth на мок-об'єкт mock_send_email. Після цього ми не будемо відправляти реальні електронні листи під час тестування.
# Цей механізм дуже корисний при створенні тестів, коли необхідно змінити якісь глобальні або системні налаштування, щоб уникнути впливу на реальну систему або, щоб змінити поведінку коду, що тестується,
# під час тестування.

# Далі client.post виконує POST-запит на вказану URL-адресу /api/auth/signup, передаючи в тілі запиту JSON-представлення даних користувача user. 
# Після відповіді нашого застосунку за допомогою assert переконуємося, що код стану відповіді сервера дорівнює 201 (успішне створення ресурсу). 
# Якщо це не так, повертаємо помилку з текстом відповіді response.text. Перевіряємо дані, що повертаються застосунком data = response.json(), витягуючи JSON-дані з відповіді сервера.
# Перевіряємо assert data["user"]["email"] == user.get("email"), що електронна пошта нового користувача дорівнює очікуваній. Перевіряємо assert "id" in data["user"], що повернуті дані містять
# ідентифікатор нового користувача, а отже, користувач був створений в базі даних.

def test_repeat_create_user(client, user):
    response = client.post(
        "/api/auth/signup",
        json=user,
    )
    assert response.status_code == 409, response.text
    data = response.json()
    assert data["detail"] == "Account already exists"


def test_login_user_not_confirmed(client, user):
    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": user.get('password')},
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] == "Email not confirmed"


def test_login_user(client, session, user):
    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    current_user.confirmed = True
    session.commit()
    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": user.get('password')},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["token_type"] == "bearer"
# Спочатку тест витягує об'єкт користувача з бази даних current_user, 
# використовуючи його адресу електронної пошти, потім встановлює властивість підтвердження користувача в True і зберігає зміни в базі даних session.commit(). 
# Нагадаємо, що, оскільки ми встановили параметр scope="module" для session, то під час виконання тестів у нашому модулі всі дані залишаються в базі даних, 
# а, значить, ми маємо доступ до користувача, який створили в тесті test_create_user.

# Після цього тест відправляє POST-запит на кінцеву точку /api/auth/login з електронною адресою та паролем користувача в якості тіла запиту.
# Зверніть увагу, що зараз ми передаємо об'єкт data, оскільки наш сервер очікує відповідь від форми з MIME-тип вмістом application/x-www-form-urlencoded.

# Потім він перевіряє, що код стану відповіді дорівнює 200 і що JSON відповіді містить поле token_type зі значенням "bearer",
# яке вказує на те, що користувач успішно пройшов аутентифікацію і отримав токен доступу.

def test_login_wrong_password(client, user):
    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": 'password'},
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] == "Invalid password"


def test_login_wrong_email(client, user):
    response = client.post(
        "/api/auth/login",
        data={"username": 'email', "password": user.get('password')},
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] == "Invalid email"
