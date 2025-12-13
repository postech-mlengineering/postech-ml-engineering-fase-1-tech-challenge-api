import pytest 
from api.models.__init__ import db
from api.__init__ import create_app

@pytest.fixture
def app():

    app = create_app(testing=True)
    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()