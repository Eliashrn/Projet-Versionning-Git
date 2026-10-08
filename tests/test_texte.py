import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.main import app
from app.texte import est_palindrome

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