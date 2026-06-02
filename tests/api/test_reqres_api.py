import requests
import pytest

BASE_URL = "https://reqres.in"

def test_get_user():
    response = requests.get(f"{BASE_URL}/api/users", params={"page": 2})
    body = response.json()
    assert response.status_code == 200
    assert body["page"] == 2
    assert len(body["data"]) > 0

def test_create_user():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }
    response = requests.post(f"{BASE_URL}/api/users", json=payload)
    body = response.json()
    
    assert response.status_code == 200
    assert "token" in body
