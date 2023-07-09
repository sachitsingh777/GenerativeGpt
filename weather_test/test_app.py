# test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_weather_existing_city(client):
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'temperature': 14, 'weather': 'Cloudy'}

def test_get_weather_non_existing_city(client):
    response = client.get('/weather/Unknown City')
    assert response.status_code == 404
    data = response.get_json()
    assert data == {'error': 'City not found'}

def test_add_weather(client):
    response = client.post('/weather', json={'city': 'Chicago', 'temperature': 18, 'weather': 'Partly Cloudy'})
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'message': 'Weather data added successfully'}

def test_add_weather_invalid_data(client):
    response = client.post('/weather', json={'city': 'Chicago', 'temperature': 18})
    assert response.status_code == 400
    data = response.get_json()
    assert data == {'error': 'Invalid data'}

def test_update_weather(client):
    response = client.put('/weather/San Francisco', json={'weather': 'Sunny'})
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'message': 'Weather data updated successfully'}

def test_update_weather_non_existing_city(client):
    response = client.put('/weather/Unknown City', json={'temperature': 25})
    assert response.status_code == 404
    data = response.get_json()
    assert data == {'error': 'City not found'}

def test_delete_weather(client):
    response = client.delete('/weather/Austin')
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'message': 'Weather data deleted successfully'}

def test_delete_weather_non_existing_city(client):
    response = client.delete('/weather/Unknown City')
    assert response.status_code == 404
    data = response.get_json()
    assert data == {'error': 'City not found'}

