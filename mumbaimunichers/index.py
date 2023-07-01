inventory = {}

def add_snack(snack_id, name, price):
    if snack_id in inventory:
        print("Snack with ID", snack_id, "already exists.")
    elif price <= 0:
        print("Price must be greater than 0.")
    else:
        inventory[snack_id] = {'name': name, 'price': price, 'available': True}
        print("Snack added successfully.")

def remove_snack(snack_id):
    if snack_id in inventory:
        del inventory[snack_id]
        print("Snack removed successfully.")
    else:
        print("Snack with ID", snack_id, "does not exist.")

def update_availability(snack_id, availability):
    if snack_id in inventory:
        inventory[snack_id]['available'] = availability
        print("Availability updated successfully.")
    else:
        print("Snack with ID", snack_id, "does not exist.")

sales_record = []

def record_sale(snack_id):
    if snack_id in inventory and inventory[snack_id]['available']:
        sales_record.append(snack_id)
        inventory[snack_id]['available'] = False
        print("Sale recorded successfully.")
    elif snack_id in inventory and not inventory[snack_id]['available']:
        print("Snack with ID", snack_id, "is already sold out.")
    else:
        print("Invalid snack ID.")

def display_menu():
    print("======= Mumbai Munchies =======")
    print("1. Add a snack")
    print("2. Remove a snack")
    print("3. Update snack availability")
    print("4. Record a sale")
    print("5. Exit")

def get_user_choice():
    choice = input("Enter your choice: ")
    return choice

def process_choice(choice):
    if choice == '1':
        snack_id = input("Enter snack ID: ")
        name = input("Enter snack name: ")
        price = float(input("Enter snack price: "))
        add_snack(snack_id, name, price)
    elif choice == '2':
        snack_id = input("Enter snack ID to remove: ")
        remove_snack(snack_id)
    elif choice == '3':
        snack_id = input("Enter snack ID to update availability: ")
        availability = input("Enter availability (yes/no): ").lower() == 'yes'
        update_availability(snack_id, availability)
    elif choice == '4':
        snack_id = input("Enter snack ID for sale: ")
        record_sale(snack_id)
    elif choice == '5':
        print("Thank you for using Mumbai Munchies!")
        exit()
    else:
        print("Invalid choice. Please try again.")

def start_application():
    while True:
        display_menu()
        choice = get_user_choice()
        process_choice(choice)


start_application()
