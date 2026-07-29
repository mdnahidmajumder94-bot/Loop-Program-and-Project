expense = []
print("\n1. Add Expense")
print("2. Total Expense")
print("3. Exit")

while True:
    choice = input("Enter your choice:")
    if choice == "1":
        amount = float(input("Enter your amount: "))
        expense.append(amount)

    elif choice == "2":
        total = sum (expense)

    elif choice == "3":
        break