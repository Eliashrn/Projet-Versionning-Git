import pytest
from fastapi.testclient import TestClient

from app.conversion import celsius_fahrenheit, euros_devise, km_miles
from app.main import app

client = TestClient(app)


# celsius_fahrenheit : normal, limite, erreur
def test_celsius_fahrenheit_ebullition():
    assert celsius_fahrenheit(100) == 212


def test_celsius_fahrenheit_zero():
    assert celsius_fahrenheit(0) == 32


def test_celsius_fahrenheit_sous_zero_absolu():
    with pytest.raises(ValueError):
        celsius_fahrenheit(-300)


# km_miles
def test_km_miles_normal():
    assert km_miles(10) == pytest.approx(6.21371)


def test_km_miles_zero():
    assert km_miles(0) == 0


def test_km_miles_negatif():
    with pytest.raises(ValueError):
        km_miles(-5)


# euros_devise
def test_euros_devise_normal():
    assert euros_devise(100, "USD") == pytest.approx(108)


def test_euros_devise_montant_zero():
    assert euros_devise(0, "USD") == 0


def test_euros_devise_devise_inconnue():
    with pytest.raises(ValueError):
        euros_devise(100, "XXX")


# routes : succès et erreur 400
def test_route_celsius_fahrenheit():
    r = client.get("/conversion/celsius-fahrenheit/100")
    assert r.status_code == 200
    assert r.json()["fahrenheit"] == 212


def test_route_km_miles_negatif():
    r = client.get("/conversion/km-miles/-5")
    assert r.status_code == 400


def test_route_euros_devise_inconnue():
    r = client.get("/conversion/euros-devise/100/XXX")
    assert r.status_code == 400