from flask import Flask, render_template, request, session, jsonify
import json
from flask_cors import CORS
from pymongo import MongoClient

import os
app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = 'your_secret_key'

# Connect to MongoDB
client = MongoClient('mongodb+srv://sachitsingh:devimeera@cluster0.uxkhuc6.mongodb.net/restaurant_app?retryWrites=true&w=majority')
db = client['restaurant_app']

# Initialize menu and orders
order_count = 0

# Load menu data from MongoDB
menu_collection = db['menu']
menu = {}
for doc in menu_collection.find():
    menu[doc['_id']] = doc

# Load orders data from MongoDB
orders_collection = db['orders']
orders = {}
for doc in orders_collection.find():
    orders[doc['_id']] = doc
    order_count = max(order_count, doc['_id'])

# Load user data from MongoDB
users_collection = db['users']
users = {}
for doc in users_collection.find():
    users[doc['_id']] = doc

# Configure image uploads



@app.route("/")
def home():
    return "Welcome to the restaurant app"


@app.route("/menu")
def get_menu():
    menu_data = []
    for dish in menu.values():
        dish_data = {
            "_id": dish["_id"],
            "dish_name": dish["dish_name"],
            "price": dish["price"],
            "availability": dish["availability"],
            "stock": dish["stock"],
            "image":dish["image"]  # Generate the image URL
        }
        menu_data.append(dish_data)

    return jsonify(menu_data)


@app.route("/orders")
def get_orders():
    return jsonify(list(orders.values()))


@app.route("/add_dish", methods=["POST"])
def add_dish():
    dish_data = request.form
    dish_id = dish_data.get("dish_id")
    dish_name = dish_data.get("dish_name")
    price = dish_data.get("price")
    availability = dish_data.get("availability")
    image = request.files["image"]

  

    menu_collection.update_one(
        {"_id": dish_id},
        {"$set": {
            "dish_name": dish_name,
            "price": float(price),
            "availability": availability == "yes",
            "stock": 0,
            "image":image  # Save the filename in the database
        }},
        upsert=True
    )

    menu[dish_id] = {
        "_id": dish_id,
        "dish_name": dish_name,
        "price": float(price),
        "availability": availability == "yes",
        "stock": 0,
        "image": image  # Include the image filename in the menu data
    }

    return jsonify(menu)


@app.route("/remove_dish", methods=["POST"])
def remove_dish():
    dish_id = request.json.get("dish_id")
    if dish_id in menu:
        menu_collection.delete_one({"__id": dish_id})
        del menu[dish_id]
        return jsonify({"message": "Dish removed successfully"})
    else:
        return jsonify({"error": "Dish not found"})


@app.route("/update_availability", methods=["POST"])
def update_availability():
    dish_id = request.json.get("dish_id")
    availability = request.json.get("availability")

    if dish_id in menu:
        menu_collection.update_one(
            {"_id": dish_id},
            {"$set": {
                "availability": availability == "yes",
                "stock": 1 if availability == "yes" else 0
            }}
        )

        menu[dish_id]["availability"] = availability == "yes"
        menu[dish_id]["stock"] = 1 if availability == "yes" else 0

    return jsonify(menu)


@app.route("/new_order", methods=["POST"])
def new_order():
    customer_name = request.json.get("customer_name")
    dish_ids = request.json.get("dish_ids")

    order_dishes = []
    for dish_id in dish_ids:
        if dish_id in menu and menu[dish_id]["availability"] and menu[dish_id]["stock"] > 0:
            order_dishes.append({
                "dish_name": menu[dish_id]["dish_name"],
                "price": menu[dish_id]["price"]
            })

            # Decrease stock by 1
            menu_collection.update_one(
                {"_id": dish_id},
                {"$inc": {"stock": -1}}
            )
            menu[dish_id]["stock"] -= 1

    if len(order_dishes) > 0:
        order_count += 1
        orders_collection.insert_one({
            "_id": order_count,
            "customer_name": customer_name,
            "dishes": order_dishes,
            "status": "received"
        })

    return jsonify(orders)


@app.route("/update_status", methods=["POST"])
def update_status():
    order_id = int(request.json.get("order_id"))
    status = request.json.get("status")

    if order_id in orders:
        orders_collection.update_one(
            {"_id": order_id},
            {"$set": {"status": status}}
        )

        orders[order_id]["status"] = status

    return jsonify(orders)


# Load user data from MongoDB
users_collection = db['users']
users = {}
for doc in users_collection.find():
    users[doc['_id']] = doc


# Login route
@app.route('/login', methods=['POST'])
def login():
    login_identifier = request.json.get('login_identifier')
    password = request.json.get('password')

    # Check if login_identifier is email or username
    user = None
    if '@' in login_identifier:
        # Login with email
        user = find_user_by_email(login_identifier)
    else:
        # Login with username
        user = find_user_by_username(login_identifier)

    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # Verify password
    if user['password'] == password:
        session['username'] = user['username']
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'error': 'Invalid password'}), 401


# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    name = request.json.get('name')
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    # Check if username or email already exists
    if find_user_by_username(username) is not None:
        return jsonify({'error': 'Username already exists'}), 400

    if find_user_by_email(email) is not None:
        return jsonify({'error': 'Email already exists'}), 400

    # Create new user
    new_user = {
        '_id': str(len(users) + 1),
        'name': name,
        'username': username,
        'email': email,
        'password': password
    }

    # Add new user to user data
    users_collection.insert_one(new_user)
    users[new_user['_id']] = new_user

    session['username'] = username

    # Return the response
    return jsonify({'username': username})


def find_user_by_username(username):
    for user in users.values():
        if user['username'] == username:
            return user
    return None


def find_user_by_email(email):
    for user in users.values():
        if user['email'] == email:
            return user
    return None


# Logout route
@app.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        username = session['username']
        session.pop('username', None)
        return jsonify({'message': f'Logged out successfully: {username}'}), 200
    else:
        return jsonify({'error': 'No active session'}), 401

if __name__ == "__main__":
    app.run()
