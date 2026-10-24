import pytest
from fastapi.testclient import TestClient

from app import math_outils as m
from app.main import app

client = TestClient(app)



def test_factorielle_normal():
    assert m.factorielle(5) == 120


def test_factorielle_limite():
    assert m.factorielle(0) == 1


def test_factorielle_erreur():
    with pytest.raises(ValueError):
        m.factorielle(-1)


def test_route_factorielle():
    assert client.get("/math/factorielle?n=5").json() == {"resultat": 120}
    assert client.get("/math/factorielle?n=-1").status_code == 400