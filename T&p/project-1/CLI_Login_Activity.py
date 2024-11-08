items = []

def add_item():
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    item_quantity = int(input("Enter item quantity: "))
    item_total_amount = item_price * item_quantity
    items.append([item_name, item_price, item_quantity, item_total_amount])
    print("Item details added successfully!!")
    admin_dashboard()

def show_item(return_to_dashboard=True):
    if not items:
        print("No items available.")
    else:
        print("\nItem details are as follows:")
        print("S.No \t Item name \t Price \t Quantity \t Total Amount")
        for i, item in enumerate(items, start=1):
            print(f"{i} \t {item[0]} \t {item[1]:.2f} \t {item[2]} \t {item[3]:.2f}")
    
    if return_to_dashboard:
        admin_dashboard()

def update_item():
    show_item(return_to_dashboard=False)
    selected_item = int(input("Enter the item number you want to update: "))
    
    if selected_item > len(items) or selected_item <= 0:
        print("Invalid item number, please try again!!")
        update_item()
    else:
        print("1. Update item name")
        print("2. Update item price")
        print("3. Update item quantity")
        print("4. Update item total amount")
        print("5. Go back to main menu")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            new_item_name = input("Enter new item name: ")
            items[selected_item - 1][0] = new_item_name
            print("Item name updated successfully!!")
        elif choice == 2:
            new_item_price = float(input("Enter new item price: "))
            items[selected_item - 1][1] = new_item_price
            print("Item price updated successfully!!")
        elif choice == 3:
            new_item_quantity = int(input("Enter new item quantity: "))
            items[selected_item - 1][2] = new_item_quantity
            print("Item quantity updated successfully!!")
        elif choice == 4:
            items[selected_item - 1][3] = items[selected_item - 1][1] * items[selected_item - 1][2]
            print("Item total amount updated successfully!!")
        elif choice == 5:
            admin_dashboard()
            return
        
        if choice == 2 or choice == 3:
            items[selected_item - 1][3] = items[selected_item - 1][1] * items[selected_item - 1][2]
        
        admin_dashboard()

def delete_item():
    if not items:
        print("No items available to delete.")
        admin_dashboard()
        return
    
    while True:
        show_item(return_to_dashboard=False)
        selected_item = int(input("Enter the item number you want to delete: "))
        if selected_item > len(items) or selected_item <= 0:
            print("Invalid item number, please try again!!")
        else:
            del items[selected_item - 1]
            print("Item deleted successfully!!")
            break
    admin_dashboard()

def admin_item_validate():
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        update_item()
    elif choice == 3:
        delete_item()
    elif choice == 4:
        show_item()
    elif choice == 0:
        main()
    else:
        print("Invalid choice, try again!!")
        admin_dashboard()

def admin_dashboard():
    print("\n======Admin Dashboard=======")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Show Item")
    print("0. Main menu")
    admin_item_validate()

def admin_validate():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "Pikachu" and password == "1234":
        admin_dashboard()
    else:
        print("Invalid username or password, please try again")
        admin_validate()

def validate():
    choice = int(input("Enter your choice: "))
    if choice == 1:
        admin_validate()
    elif choice == 2:
        print("User Login (Not implemented)")
    elif choice == 0:
        print("Thank you!!")
    else:
        print("Invalid Choice, try again!!")
        main()

def main():
    print("\n\n=====Main Menu=====")
    print("1. Admin")
    print("2. User")
    print("0. Exit")
    validate()

main()