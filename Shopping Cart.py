cart = []

print("\n1.add item")
print("2.sell item")
print("3.show cart")
print("4.Exit")

while True:
    choice = input("Enter your choice:")
    if choice == "1":
        item = input("Item name:")
        cart.append(item)

    elif choice == "2":
        sell_item = input("Sell item name:")
        cart.remove(sell_item)

    elif choice == "3":
        print(cart)

    elif choice == "4":
        print("Thank you for coming our Shopping Cart!")
        break