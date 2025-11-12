import pytest
import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(__file__))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page returns 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_health_endpoint(client):
    """Test the health endpoint returns healthy status"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'service' in data

def test_invalid_route(client):
    """Test invalid route returns 404"""
    response = client.get('/invalid-route')
    assert response.status_code == 404

def test_app_creation():
    """Test that app instance is created"""
    assert app is not None
    assert hasattr(app, 'route')
