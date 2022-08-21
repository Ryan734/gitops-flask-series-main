import pytest

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    result = client.get('/')
    assert b'hello' in result.data

def test_cluster_identity(client):
    result = client.get('/cluster')
    assert b'This is service1 in cluster cluster1' in result.data
