import pytest

from app import app, db
from app.models.models import Pais

@pytest.fixture
def cliente():
    with app.app_context():
        db.create_all()

    cliente = app.test_client()
    yield cliente

    with app.app_context():
        db.session.rollback()

def test_get_all_paises_fail(cliente):
    response = cliente.get('api/v1/pais')
    assert response.status_code == 404


def test_get_all_paises(cliente):
    #Act
    response = cliente.get('/pais')
    
    #Assert
    data = response.json

    # assert len(data) == 3
    assert data[0] == dict(id=1, nombre="Argentina")
    assert response.status_code == 200


def test_create_pais(cliente):
    # Arrange
    data = dict(nombre="Japon")

    # Act
    response = cliente.post("/pais", json=data)
    
    #Assert
    assert response.status_code == 201
    
    with app.app_context():
        pais = Pais.query.order_by(Pais.id.desc()).first()

    assert pais.nombre == "Japon"