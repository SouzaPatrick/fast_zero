from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        "/users/",
        json={
            "username": "Usuário Teste",
            "email": "teste@exemple.com",
            "password": "1232456",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "Usuário Teste",
        "email": "teste@exemple.com",
        "id": 1,
    }
