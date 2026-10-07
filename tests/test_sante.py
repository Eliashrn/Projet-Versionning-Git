from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sante():
    reponse = client.get("/sante")
    assert reponse.status_code == 200
    assert reponse.json() == {"status": "ok"}