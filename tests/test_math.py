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



def test_est_premier_normal():
    assert m.est_premier(7) is True
    assert m.est_premier(9) is False


def test_est_premier_limite():
    assert m.est_premier(0) is False
    assert m.est_premier(1) is False
    assert m.est_premier(2) is True


def test_est_premier_erreur():
    with pytest.raises(ValueError):
        m.est_premier(-5)


def test_route_est_premier():
    assert client.get("/math/est_premier?n=7").json() == {"resultat": True}
    assert client.get("/math/est_premier?n=-5").status_code == 400