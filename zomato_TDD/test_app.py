import json
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_signup(client):
    # Test successful signup
    user_data = {
        'email': 'test@example.com',
        'password': 'password'
    }
    response = client.post('/signup', json=user_data)
    assert response.status_code == 200
    assert 'user_id' in response.json['data']
    assert response.json['message'] == 'User created successfully.'

    # Test signup with missing data
    response = client.post('/signup', json={})
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid user data.'


def test_login(client):
    # Test successful login
    user_data = {
        'email': 'test@example.com',
        'password': 'password'
    }
    response = client.post('/login', json=user_data)
    assert response.status_code == 200
    assert 'user_id' in response.json['data']
    assert response.json['message'] == 'Login successful.'

    # Test login with incorrect credentials
    user_data = {
        'email': 'test@example.com',
        'password': 'wrongpassword'
    }
    response = client.post('/login', json=user_data)
    assert response.status_code == 401
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid credentials.'


def test_menu(client):
    response = client.get('/')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_add_dish(client):
    # Test successful dish addition
    dish_data = {
        'name': 'Test Dish',
        'price': 10.99
    }
    response = client.post('/menu/add', json=dish_data)
    assert response.status_code == 200
    assert 'dish_id' in response.json['data']
    assert response.json['message'] == 'Dish added successfully.'

    # Test dish addition with missing data
    response = client.post('/menu/add', json={})
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid dish data.'


def test_remove_dish(client):
    # Add a dish for removal
    dish_data = {
        'name': 'Test Dish',
        'price': 10.99
    }
    response = client.post('/menu/add', json=dish_data)
    assert response.status_code == 200
    dish_id = response.json['data']['dish_id']

    # Test successful dish removal
    response = client.delete(f'/menu/remove/{dish_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Dish removed successfully.'

    # Test dish removal for non-existent dish
    response = client.delete('/menu/remove/999')
    assert response.status_code == 404
    assert response.json['error'] == 'Dish not found.'


def test_update_dish(client):
    # Add a dish for updating
    dish_data = {
        'name': 'Test Dish',
        'price': 10.99
    }
    response = client.post('/menu/add', json=dish_data)
    assert response.status_code == 200
    dish_id = response.json['data']['dish_id']

    # Test successful dish update
    updated_data = {
        'name': 'Updated Dish',
        'price': 15.99
    }
    response = client.put(f'/menu/update_dish/{dish_id}', json=updated_data)
    assert response.status_code == 200
    assert response.json['message'] == 'Dish updated successfully.'

    # Test dish update for non-existent dish
    response = client.put('/menu/update_dish/999', json=updated_data)
    assert response.status_code == 404
    assert response.json['error'] == 'Dish not found.'


def test_place_order(client):
    # Add a dish for placing an order
    dish_data = {
        'name': 'Test Dish',
        'price': 10.99
    }
    response = client.post('/menu/add', json=dish_data)
    assert response.status_code == 200
    dish_id = response.json['data']['dish_id']

    # Test successful order placement
    order_data = {
        'dish_id': dish_id,
        'quantity': 2
    }
    response = client.post('/order/new', json=order_data)
    assert response.status_code == 200
    assert 'order_id' in response.json['data']
    assert response.json['message'] == 'Order placed successfully.'

    # Test order placement with missing data
    response = client.post('/order/new', json={})
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid order data.'


# Add tests for other API endpoints...


if __name__ == '__main__':
    pytest.main()
