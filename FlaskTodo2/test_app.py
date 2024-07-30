# test_app.py
import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_add(client):
    rv = client.post('/add', data={'title': 'Test Todo'})
    assert rv.status_code == 302  # redirect to index
    assert Todo.query.count() == 1

def test_update(client):
    todo = Todo(title='Test Todo', complete=False)
    db.session.add(todo)
    db.session.commit()
    rv = client.get(f'/update/{todo.id}')
    assert rv.status_code == 302  # redirect to index
    assert Todo.query.first().complete == True

def test_delete(client):
    todo = Todo(title='Test Todo', complete=False)
    db.session.add(todo)
    db.session.commit()
    rv = client.get(f'/delete/{todo.id}')
    assert rv.status_code == 302  # redirect to index
    assert Todo.query.count() == 0
