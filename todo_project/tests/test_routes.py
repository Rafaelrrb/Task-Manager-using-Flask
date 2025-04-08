import pytest
from todo_project import app, db
from flask import url_for

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data

def test_register_page_loads(client):
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data

def test_404(client):
    response = client.get("/nonexistentpage")
    assert response.status_code == 404
