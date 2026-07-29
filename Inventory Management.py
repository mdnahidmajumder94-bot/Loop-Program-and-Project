inventory = {}

print("Welcome to our Shop")
print("1. Add Product")
print("2. Show Product")
print("3. update Product")
print("4. Exit")

while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        name = input("Enter product name:")
        price = float(input("Enter product price:"))
        inventory[name] = price

    elif choice == 2:
        for name, price in inventory.items():
            print(f"{name} -> {price}")

    elif choice == 3:
        name = input("Enter product name:")
        if name in inventory:
            inventory[name] = input("Enter update product price:")

    elif choice == 4:
        print("Thank you for shopping")
        break

