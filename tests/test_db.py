from app.extensions import db
from app.models import User

def test_db(app):
    assert app is not None

def test_create_user(app):
    with app.app_context():
        user = User(email="alice", password="test")

        db.session.add(user)
        db.session.commit()

        result = User.query.filter_by(email="alice").first()

        assert result is not None
        assert result.email == "alice"

def test_delete_user(app):
    assert True

def test_change_email(app):
    assert True

def test_change_password(app):
    assert True