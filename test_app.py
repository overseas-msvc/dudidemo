
import json
import pytest
from app import app

@pytest.fixture
def client():
    """Provides a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/hello", json={'name': 'sample_string'})
    assert response.status_code == 200
    assert json.loads(response.get_data()) == "reply from endpoint hello, data = {'name': 'sample_string'}"

def test_bye(client):
    response = client.get("/bye", json={})
    assert response.status_code == 200
    assert json.loads(response.get_data()) == "reply from endpoint bye"
