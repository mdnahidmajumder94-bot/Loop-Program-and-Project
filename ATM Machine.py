Balance = 0

print("Welcome to ATM Machine")
print("1.chack balance")
print("2.deposit")
print("3.withdraw")
print("4.exit")

while True:
    choice = input("Enter your choice: ")

    # chack balance
    if choice == "1":
        print("Your Balance = ", Balance)

    # deposit balance
    elif choice == "2":
        add_balance = int(input("Enter your deposit amount: "))
        Balance += add_balance

    # withdraw  balance
    elif choice == "3":
        out_balance = int(input("Enter your withdraw amount: "))
        Balance -= out_balance

    # exit the ATM machine
    elif choice == "4":
        print("Thank you for using ATM Machine")
        break



