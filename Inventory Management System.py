# Inventory Management System 

# Stores inventory data as a list of dictionaries
inventory = [
    {"name": "Laptop", "quantity": 10, "price": 999.99},
    {"name": "Smartphone", "quantity": 25, "price": 499.99},
    {"name": "Headphones", "quantity": 50, "price": 199.99},
    {"name": "Monitor", "quantity": 15, "price": 299.99},
    {"name": "Keyboard", "quantity": 30, "price": 49.99}
]

# 1. Function to display all products in inventory
def view_all_products(inventory):
    if not inventory:
        print("\nNo products in inventory.")
        return
    for product in inventory:
        print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")

# 2.Function to add a new product to inventory
def add_new_product(inventory):
    name = input("Enter product name: ")
    if name == "":
        print("Product name cannot be empty.")
        return
    category = input("Enter product category: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    
    new_product = [{"name": name, "category": category, "quantity": quantity, "price": price}]
    inventory.append(new_product[0])

# 3. Function to update quantity of an existing product
def update_quantity(inventory):
    name = input("Enter product name to update: ")
    for product in inventory:
        if product["name"] == name:
            new_quantity = int(input("Enter new quantity: "))
            product["quantity"] = new_quantity
            print(f"Updated quantity for {name} to {new_quantity}")
            return
    print(f"Product '{name}' not found.")

# 4. Function to search for a product by name
def search_product(inventory):
    name = input("Enter product name to search: ")
    for product in inventory:
        if product["name"] == name:
            print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")
            return
    print(f"Product '{name}' not found.")

# 5. Function to remove a product from inventory
def remove_product(inventory):
    name = input("Enter product name to remove: ")
    for product in inventory:
        if product["name"] == name:
            inventory.remove(product)
            print(f"Removed product '{name}' from inventory.")
            return
    print(f"Product '{name}' not found.")

# 6. Function to calculate total inventory value
def calculate_inventory_value(inventory):
    total_value = sum(product["quantity"] * product["price"] for product in inventory)
    print(f"Total inventory value: ${total_value:.2f}")

# 7. Function to display low stock products (quantity < 5)
def low_stock_alert(inventory):
    low_stock_products = [product for product in inventory if product["quantity"] < 5]
    if not low_stock_products:
        print("No low stock products.")
        return
    print("Low stock products:")
    for product in low_stock_products:
        print(f"Name: {product['name']}, Quantity: {product['quantity']}")

# Displays main menu
def display_menu():
    print("\n" + "="*40) 
    print("   INVENTORY MANAGEMENT SYSTEM") 
    print("="*40) 
    print("1. View all products") 
    print("2. Add new product") 
    print("3. Update quantity") 
    print("4. Search product") 
    print("5. Remove product") 
    print("6. Calculate inventory value") 
    print("7. Low stock alert") 
    print("8. Exit") 
    print("="*40)

# Main program loop
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("\nChoice: ")
        if choice == "1":
            view_all_products(inventory)
        elif choice == "2":
            add_new_product(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            remove_product(inventory)
        elif choice == "6":
            calculate_inventory_value(inventory)
        elif choice == "7":
            low_stock_alert(inventory)
        elif choice == "8":
            print("\nThank you for using Inventory Manager!")
            break
        else:
            print("Invalid choice. Please try again.")