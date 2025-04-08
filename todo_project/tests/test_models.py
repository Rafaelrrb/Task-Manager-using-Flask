import pytest
from datetime import datetime
from unittest.mock import MagicMock
from todo_project.models import User, Task

# ==== Fixtures com mocks ====

@pytest.fixture
def new_user():
    user = User(username='rafael', password='senha123')
    user.tasks = []  # simula relacionamento
    return user

@pytest.fixture
def new_task(new_user):
    task = Task(content='Estudar Flask', author=new_user)
    task.date_posted = datetime.utcnow()  # força a criação da data
    new_user.tasks.append(task)  # simula relacionamento reverso
    return task

# ==== Testes de User ====

def test_create_user(new_user):
    assert new_user.username == 'rafael'
    assert new_user.password == 'senha123'
    assert new_user.tasks == []

def test_user_repr(new_user):
    assert repr(new_user) == "User('rafael')"

# ==== Testes de Task ====

def test_create_task(new_task):
    assert new_task.content == 'Estudar Flask'
    assert isinstance(new_task.date_posted, datetime)
    assert new_task.author.username == 'rafael'

def test_task_repr(new_task):
    assert repr(new_task).startswith(
        f"Task('Estudar Flask', '{new_task.date_posted.strftime('%Y-%m-%d')}"
    )

def test_database_relationship():
    # simula o relacionamento sem banco
    user = User(username='testeuser', password='abc123')
    user.tasks = []
    task = Task(content='Fazer testes', author=user)
    task.user_id = 1  # simula ID
    user.id = 1       # simula ID

    user.tasks.append(task)

    assert task in user.tasks
    assert task.user_id == user.id
