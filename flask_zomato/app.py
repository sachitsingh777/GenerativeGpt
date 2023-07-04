from flask import Flask, render_template, request, redirect

import pickle

app = Flask(__name__)

# Initialize menu and orders
menu = {}
orders = {}
order_count = 0

# Load menu data from file using pickle
try:
    with open("menu.pickle", "rb") as file:
        menu = pickle.load(file)
except FileNotFoundError:
    pass

# Load orders data from file using pickle
try:
    with open("orders.pickle", "rb") as file:
        orders = pickle.load(file)
        order_count = max(orders.keys()) + 1
except FileNotFoundError:
    pass


@app.route("/")
def home():
    return render_template("index.html", menu=menu, orders=orders)


@app.route("/add_dish", methods=["POST"])
def add_dish():
    global menu
    dish_id = request.form.get("dish_id")
    dish_name = request.form.get("dish_name")
    price = request.form.get("price")
    availability = request.form.get("availability")

    menu[dish_id] = {
        "dish_name": dish_name,
        "price": float(price),
        "availability": availability == "yes"
    }

    # Save menu data to file using pickle
    with open("menu.pickle", "wb") as file:
        pickle.dump(menu, file)

    return redirect("/")


@app.route("/remove_dish", methods=["POST"])
def remove_dish():
    global menu
    dish_id = request.form.get("dish_id")
    if dish_id in menu:
        del menu[dish_id]

        # Save menu data to file using pickle
        with open("menu.pickle", "wb") as file:
            pickle.dump(menu, file)

    return redirect("/")


@app.route("/update_availability", methods=["POST"])
def update_availability():
    global menu
    dish_id = request.form.get("dish_id")
    availability = request.form.get("availability")

    if dish_id in menu:
        menu[dish_id]["availability"] = availability == "yes"

        # Save menu data to file using pickle
        with open("menu.pickle", "wb") as file:
            pickle.dump(menu, file)

    return redirect("/")


@app.route("/new_order", methods=["POST"])
def new_order():
    global orders, order_count
    customer_name = request.form.get("customer_name")
    dish_ids = request.form.getlist("dish_ids")

    order_dishes = []
    for dish_id in dish_ids:
        if dish_id in menu and menu[dish_id]["availability"]:
            order_dishes.append({
                "dish_name": menu[dish_id]["dish_name"],
                "price": menu[dish_id]["price"]
            })

    if len(order_dishes) > 0:
        order_count += 1
        orders[order_count] = {
            "customer_name": customer_name,
            "dishes": order_dishes,
            "status": "received"
        }

        # Save orders data to file using pickle
        with open("orders.pickle", "wb") as file:
            pickle.dump(orders, file)

    return redirect("/")


@app.route("/update_status", methods=["POST"])
def update_status():
    global orders
    order_id = int(request.form.get("order_id"))
    status = request.form.get("status")

    if order_id in orders:
        orders[order_id]["status"] = status

        # Save orders data to file using pickle
        with open("orders.pickle", "wb") as file:
            pickle.dump(orders, file)

    return redirect("/")


if __name__ == "__main__":
    app.run()