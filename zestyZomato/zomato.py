menu = {}
orders = {}
order_id_counter = 1


def add_dish(dish_id, name, price):
    if dish_id in menu:
        print("Dish with ID", dish_id, "already exists.")
    elif name in [dish['name'] for dish in menu.values()]:
        print("Dish with name", name, "already exists.")
    elif price <= 0:
        print("Price must be greater than 0.")
    else:
        menu[dish_id] = {'name': name, 'price': price, 'available': True}
        print("Dish added successfully.")

def remove_dish(identifier):
    removed_dishes = []
    for dish_id, dish in menu.items():
        if dish['name'] == identifier or dish_id == identifier:
            removed_dishes.append(dish_id)

    if not removed_dishes:
        print("Dish with name or ID", identifier, "does not exist.")
    else:
        for dish_id in removed_dishes:
            del menu[dish_id]
        print("Dish(s) with name or ID", identifier, "removed successfully.")


def update_availability(dish_id, availability):
    if dish_id in menu:
        menu[dish_id]['available'] = availability
        print("Availability updated successfully.")
    else:
        print("Dish with ID", dish_id, "does not exist.")


def take_order(customer_name, dish_ids):
    global order_id_counter
    order_items = []
    for dish_id in dish_ids:
        if dish_id in menu and menu[dish_id]['available']:
            order_items.append({'dish_id': dish_id, 'name': menu[dish_id]['name']})
            menu[dish_id]['available'] = False
        elif dish_id in menu and not menu[dish_id]['available']:
            print("Dish with ID", dish_id, "is not available.")
        else:
            print("Invalid dish ID:", dish_id)
            return
    orders[order_id_counter] = {'customer_name': customer_name, 'order_items': order_items, 'status': 'received'}
    print("Order placed successfully. Order ID:", order_id_counter)
    order_id_counter += 1


def update_order_status(order_id, status):
    if order_id in orders:
        orders[order_id]['status'] = status
        print("Order status updated successfully.")
    else:
        print("Order with ID", order_id, "does not exist.")



def review_orders():
    print("======= Zomato Chronicles: Order Review =======")
    for order_id, order in orders.items():
        print("Order ID:", order_id)
        print("Customer Name:", order['customer_name'])
        print("Status:", order['status'])
        print("Ordered Items:")
        for item in order['order_items']:
            print("- Dish ID:", item['dish_id'])
            print("  Dish Name:", item['name'])
        print()

def display_menu():
    print("======= Zomato Chronicles: Menu Management =======")
    print("1. Add a dish")
    print("2. Remove a dish")
    print("3. Update dish availability")
    print("4. Take a new order")
    print("5. Update order status")
    print("6. Review all orders")
    print("7. Menu")
    print("8. Exit")

def display_menu_items():
    print("======= Zesty Zomato Menu =======")
    for dish_id, dish in menu.items():
        if dish['available']:
            print(f"{dish['name']} (ID: {dish_id}) - ${dish['price']}")
    print("===============================")

def get_user_choice():
    choice = input("Enter your choice: ")
    return choice


def process_choice(choice):
    if choice == '1':
        dish_id = input("Enter dish ID: ")
        name = input("Enter dish name: ")
        price = float(input("Enter dish price: "))
        add_dish(dish_id, name, price)
    elif choice == '2':
        dish_id = input("Enter dish ID to remove: ")
        remove_dish(dish_id)
    elif choice == '3':
        dish_id = input("Enter dish ID to update availability: ")
        availability = input("Enter availability (yes/no): ").lower() == 'yes'
        update_availability(dish_id, availability)
    elif choice == '4':
        customer_name = input("Enter customer name: ")
        dish_ids = input("Enter dish IDs (separated by commas): ").split(",")
        dish_ids = [dish_id.strip() for dish_id in dish_ids]
        take_order(customer_name, dish_ids)
    elif choice == '5':
        order_id = int(input("Enter order ID to update status: "))
        status = input("Enter new status: ")
        update_order_status(order_id, status)
    elif choice == '6':
        review_orders()
    elif choice == '7':
        display_menu_items() 
    elif choice == '8':
        print("Thank you for using Zomato Chronicles: The Great Food Fiasco!")
        exit()
    else:
        print("Invalid choice. Please try again.")


def start_application():
    while True:
        display_menu()
        choice = get_user_choice()
        process_choice(choice)

start_application()
