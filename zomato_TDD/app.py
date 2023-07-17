import json
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
from pymongo import MongoClient
import ssl

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app, cors_allowed_origins='*')

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://sachitsingh:devimeera@cluster0.uxkhuc6.mongodb.net/luscious?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = client["restaurant"]
menu_collection = db["menu"]
orders_collection = db["orders"]
users_collection = db["users"]


def get_dish_by_id(dish_id):
    return menu_collection.find_one({"_id": dish_id})


def update_dish_availability(dish_id, availability):
    menu_collection.update_one({"_id": dish_id}, {"$set": {"availability": availability}})


def get_order_by_id(order_id):
    return orders_collection.find_one({"_id": order_id})


def add_order(order_data):
    result = orders_collection.insert_one(order_data)
    return result.inserted_id


def update_order_status(order_id, status):
    orders_collection.update_one({"_id": order_id}, {"$set": {"status": status}})


def get_user_by_email(email):
    return users_collection.find_one({"email": email})


def create_user(user_data):
    result = users_collection.insert_one(user_data)
    return result.inserted_id


def generate_response(data=None, message=None, error=None, status_code=200):
    response = {"status": status_code}
    if data:
        response["data"] = data
    if message:
        response["message"] = message
    if error:
        response["error"] = error
    return jsonify(response), status_code


@app.route('/signup', methods=['POST'])
def signup():
    user_data = request.json
    if not user_data or 'email' not in user_data or 'password' not in user_data:
        return generate_response(error="Invalid user data.", status_code=400)

    existing_user = get_user_by_email(user_data['email'])
    if existing_user:
        return generate_response(error="User already exists.", status_code=400)

    user_id = create_user(user_data)
    return generate_response(data={"user_id": str(user_id)}, message="User created successfully.")


@app.route('/login', methods=['POST'])
def login():
    user_data = request.json
    if not user_data or 'email' not in user_data or 'password' not in user_data:
        return generate_response(error="Invalid user data.", status_code=400)

    user = get_user_by_email(user_data['email'])
    if not user or user['password'] != user_data['password']:
        return generate_response(error="Invalid credentials.", status_code=401)

    return generate_response(data={"user_id": str(user['_id'])}, message="Login successful.")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():
    menu_data = list(menu_collection.find({}, {'_id': 0}))
    return generate_response(data=menu_data)


@app.route('/menu/add', methods=['POST'])
def add_dish():
    dish_data = request.json
    if not dish_data or 'name' not in dish_data or 'price' not in dish_data:
        return generate_response(error="Invalid dish data.", status_code=400)

    dish_id = menu_collection.insert_one(dish_data).inserted_id
    return generate_response(data={"dish_id": str(dish_id)}, message="Dish added successfully.")


@app.route('/menu/remove/<int:dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    dish = get_dish_by_id(dish_id)
    if not dish:
        return generate_response(error="Dish not found.", status_code=404)

    menu_collection.delete_one({"_id": dish_id})
    return generate_response(message="Dish removed successfully.")


@app.route('/menu/update_dish/<int:dish_id>', methods=['PUT'])
def update_dish(dish_id):
    dish = get_dish_by_id(dish_id)
    if not dish:
        return generate_response(error="Dish not found.", status_code=404)

    updated_data = request.json
    if not updated_data or 'name' not in updated_data or 'price' not in updated_data:
        return generate_response(error="Invalid updated dish data.", status_code=400)

    menu_collection.update_one({"_id": dish_id}, {"$set": updated_data})
    return generate_response(message="Dish updated successfully.")


@app.route('/order/new', methods=['POST'])
def place_order():
    order_data = request.json
    if not order_data or 'dish_id' not in order_data or 'quantity' not in order_data:
        return generate_response(error="Invalid order data.", status_code=400)

    dish = get_dish_by_id(order_data['dish_id'])
    if not dish or not dish['availability']:
        return generate_response(error="Dish not available.", status_code=400)

    order_data['status'] = 'Placed'
    order_id = add_order(order_data)
    socketio.emit('new_order', {'order_id': str(order_id)}, broadcast=True)

    return generate_response(data={"order_id": str(order_id)}, message="Order placed successfully.")


@app.route('/order/update_status', methods=['PUT'])
def update_order():
    update_data = request.json
    if not update_data or 'order_id' not in update_data or 'status' not in update_data:
        return generate_response(error="Invalid update data.", status_code=400)

    order = get_order_by_id(update_data['order_id'])
    if not order:
        return generate_response(error="Order not found.", status_code=404)

    update_order_status(update_data['order_id'], update_data['status'])
    socketio.emit('order_update', {'order_id': str(update_data['order_id']), 'status': update_data['status']},
                  broadcast=True)

    return generate_response(message="Order status updated successfully.")


@app.route('/orders/<user_role>/<user_email>')
def get_orders(user_role, user_email):
    user = get_user_by_email(user_email)
    if not user or user['role'] != user_role:
        return generate_response(error="Unauthorized access.", status_code=401)

    if user_role == 'admin':
        order_data = list(orders_collection.find({}, {'_id': 0}))
    else:
        order_data = list(orders_collection.find({'email': user_email}, {'_id': 0}))

    return generate_response(data=order_data)


@socketio.on('connect')
def handle_connect():
    print('Client connected.')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected.')


if __name__ == '__main__':
    socketio.run(app, debug=True)
