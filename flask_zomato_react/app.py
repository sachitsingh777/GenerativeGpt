from flask import Flask, render_template, request, session, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = 'your_secret_key'

# Initialize menu and orders

order_count = 0

# Load menu data from file using JSON
try:
    with open("menu.json", "r") as file:
        menu = json.load(file)
except EOFError:  # Handle empty file
                menu = []
except FileNotFoundError:
        menu = []
# Load orders data from file using JSON
try:
    with open("orders.json", "r") as file:
        orders = json.load(file)
        order_count = max(orders.keys()) + 1
except EOFError:  # Handle empty file
                menu = []
except FileNotFoundError:
        menu = []


@app.route("/")
def home():
    return "Welcome to the restaurant app"

@app.route("/menu")
def get_menu():
    return jsonify(menu)

@app.route("/orders")
def get_orders():
    return jsonify(orders)


@app.route("/add_dish", methods=["POST"])
def add_dish():
    dish_data = request.json
    dish_id = dish_data.get("dish_id")
    dish_name = dish_data.get("dish_name")
    price = dish_data.get("price")
    availability = dish_data.get("availability")

    menu[dish_id] = {
        "dish_name": dish_name,
        "price": float(price),
        "availability": availability == "yes",
        "stock": 0  # Initialize stock to 0
    }

    # Save menu data to file using JSON
    with open("menu.json", "w") as file:
        json.dump(menu, file, indent=4)

    return jsonify(menu)


@app.route("/remove_dish", methods=["POST"])
def remove_dish():
    dish_id = request.json.get("dish_id")
    if dish_id in menu:
        del menu[dish_id]

        # Save menu data to file using JSON
        with open("menu.json", "w") as file:
            json.dump(menu, file, indent=4)

    return jsonify(menu)


@app.route("/update_availability", methods=["POST"])
def update_availability():
    dish_id = request.json.get("dish_id")
    availability = request.json.get("availability")

    if dish_id in menu:
        menu[dish_id]["availability"] = availability == "yes"

        # Update stock based on availability
        if availability == "yes":
            menu[dish_id]["stock"] = 1
        else:
            menu[dish_id]["stock"] = 0

        # Save menu data to file using JSON
        with open("menu.json", "w") as file:
            json.dump(menu, file, indent=4)

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
            menu[dish_id]["stock"] -= 1

    if len(order_dishes) > 0:
        global order_count
        order_count += 1
        orders[order_count] = {
            "customer_name": customer_name,
            "dishes": order_dishes,
            "status": "received"
        }

        # Save orders data to file using JSON
        with open("orders.json", "w") as file:
            json.dump(orders, file, indent=4)

        # Save updated menu data to file using JSON
        with open("menu.json", "w") as file:
            json.dump(menu, file, indent=4)

    return jsonify(orders)


@app.route("/update_status", methods=["POST"])
def update_status():
    order_id = int(request.json.get("order_id"))
    status = request.json.get("status")

    if order_id in orders:
        orders[order_id]["status"] = status

        # Save orders data to file using JSON
        with open("orders.json", "w") as file:
            json.dump(orders, file, indent=4)

    return jsonify(orders)


# Load user data from JSON file
users = {}  # Default empty dictionary

try:
    with open('users.json', 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    print("User data file not found. Using empty dictionary.")


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
        'name': name,
        'username': username,
        'email': email,
        'password': password
    }

    # Add new user to user data
    user_id = str(len(users) + 1)
    users[user_id] = new_user

    # Save user data to JSON file
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

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
