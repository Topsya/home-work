from unittest.mock import MagicMock, patch

import pytest

from jwt_na_fast_api.database.models import User
from jwt_na_fast_api.services.auth import auth_service


@pytest.fixture()
def token(client, user, session, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("jwt_na_fast_api.routes.auth.send_email", mock_send_email)
    client.post("/api/auth/signup", json=user)
    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    current_user.confirmed = True
    session.commit()
    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": user.get('password')},
    )
    data = response.json()
    return data["access_token"]


def test_create_contact(client, token):
    with patch.object(auth_service, 'r') as r_mock:
        r_mock.get.return_value = None
        response = client.post(
            "/api/contacts",
            json={"name": "test_contact"},
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["name"] == "test_contact"
        assert "id" in data


def test_read_contact(client, token):
    with patch.object(auth_service, 'r') as r_mock:
        r_mock.get.return_value = None
        response = client.get(
            "/api/contacts/1",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "test_contact"
        assert "id" in data


def test_read_contact_not_found(client, token):
    with patch.object(auth_service, 'r') as r_mock:
        r_mock.get.return_value = None
        response = client.get(
            "/api/contacts/2",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 404, response.text
        data = response.json()
        assert data["detail"] == "Contact not found"


def test_read_contacts(client, token):
    with patch.object(auth_service, 'r') as r_mock:
        r_mock.get.return_value = None
        response = client.get(
            "/api/contacts",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert isinstance(data, list)
        assert data[0]["name"] == "test_contact"
        assert "id" in data[0]


def test_update_contact(client, token):
    with patch.object(auth_service, 'r') as r_mock:
        r_mock.get.return_value = None
        response = client.put(
            "/api/contacts/1",
            json={"name": "new_test_contact"},
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "new_test_contact"
        assert "id" in data


def test_update_contact_not_found(client, token):
    with patch.object(auth_service, 'r') as r_mock:
        r_mock.get.return_value = None
        response = client.put(
            "/api/contacts/2",
            json={"name": "new_test_contact"},
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 404, response.text
        data = response.json()
        assert data["detail"] == "Contact not found"


def test_remove_contact(client, token):
    with patch.object(auth_service, 'r') as r_mock:
        r_mock.get.return_value = None
        response = client.delete(
            "/api/contacts/1",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "new_test_contact"
        assert "id" in data


def test_repeat_remove_contact(client, token):
    with patch.object(auth_service, 'r') as r_mock:
        r_mock.get.return_value = None
        response = client.delete(
            "/api/contacts/1",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 404, response.text
        data = response.json()
        assert data["detail"] == "Contact not found"