contact = {}

print("\n1.Add Number")
print("2.Search contact")
print("3.Exit")

while True:
    choice = input("Enter your choice:")
    if choice == "1":
        number = input("Enter your phone number: ")
        name = input("Enter your name: ")
        contact[name]= number

    elif choice == "2":
        for name,number in contact.items():
            print(name,":",number)

    elif choice == "3":
        break