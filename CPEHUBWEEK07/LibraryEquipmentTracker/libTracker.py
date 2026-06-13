# Library & Equipment Tracker
# Uses: lists, functions, list comprehensions, while loop

inventory = [
    ["Arduino Starter Kit", "Available"],
    ["Digital Multimeter", "Borrowed"],
    ["Python Crash Course Book", "Available"],
    ["Raspberry Pi 4", "Available"]
]


def borrow_item(item_name):
    for item in inventory:
        if item[0].lower() == item_name.lower():
            if item[1] == "Available":
                item[1] = "Borrowed"
                print(f"  '{item[0]}' has been borrowed. Good luck!")
            else:
                print(f"  Sorry, '{item[0]}' is already borrowed. Check back later.")
            return
    print(f"  Item '{item_name}' not found in inventory.")


def return_item(item_name):
    for item in inventory:
        if item[0].lower() == item_name.lower():
            if item[1] == "Borrowed":
                item[1] = "Available"
                print(f"  '{item[0]}' has been returned. Thanks!")
            else:
                print(f"  '{item[0]}' was not borrowed in the first place.")
            return
    print(f"  Item '{item_name}' not found in inventory.")


def add_new_item(item_name):
    inventory.append([item_name, "Available"])
    print(f"  '{item_name}' added to inventory.")


def view_available():
    available = [item for item in inventory if item[1] == "Available"]
    if available:
        print("\n  Available Items:")
        for item in available:
            print(f"    - {item[0]}")
    else:
        print("  No items available right now.")


def search_by_keyword(keyword):
    results = [item for item in inventory if keyword.lower() in item[0].lower()]
    if results:
        print(f"\n  Results for '{keyword}':")
        for item in results:
            print(f"    - {item[0]} [{item[1]}]")
    else:
        print(f"  No items found with keyword '{keyword}'.")


def view_all():
    print("\n  Full Inventory:")
    for item in inventory:
        print(f"    - {item[0]}: {item[1]}")


while True:
    print("\n===== CPE Library Tracker =====")
    print("  1. View all items")
    print("  2. View available items")
    print("  3. Borrow an item")
    print("  4. Return an item")
    print("  5. Add new item")
    print("  6. Search by keyword")
    print("  7. Exit")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        view_all()
    elif choice == "2":
        view_available()
    elif choice == "3":
        name = input("  Item to borrow: ").strip()
        borrow_item(name)
    elif choice == "4":
        name = input("  Item to return: ").strip()
        return_item(name)
    elif choice == "5":
        name = input("  New item name: ").strip()
        add_new_item(name)
    elif choice == "6":
        keyword = input("  Enter keyword: ").strip()
        search_by_keyword(keyword)
    elif choice == "7":
        print("  Exiting. Bye!")
        break
    else:
        print("  Invalid choice. Try again.")