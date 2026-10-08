import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.main import app
from app.texte import compter_voyelles, est_palindrome

client = TestClient(app)


def test_est_palindrome_normal():
    assert est_palindrome("kayak") is True
    assert est_palindrome("bonjour") is False


def test_est_palindrome_limite():
    assert est_palindrome("a") is True
    assert est_palindrome("Ressasser") is True


def test_est_palindrome_erreur():
    with pytest.raises(HTTPException) as info:
        est_palindrome("")
    assert info.value.status_code == 400


def test_route_est_palindrome():
    r = client.get("/texte/est_palindrome/kayak")
    assert r.status_code == 200
   
   
    assert r.json() == {"mot": "kayak", "resultat": True}
def test_compter_voyelles_normal():
    assert compter_voyelles("bonjour") == 3


def test_compter_voyelles_limite():
    assert compter_voyelles("Éléphant") == 3
    assert compter_voyelles("bcd") == 0


def test_compter_voyelles_erreur():
    with pytest.raises(HTTPException) as info:
        compter_voyelles("")
    assert info.value.status_code == 400


def test_route_compter_voyelles():
    r = client.get("/texte/compter_voyelles/bonjour")
    assert r.status_code == 200
    assert r.json() == {"texte": "bonjour", "resultat": 3}