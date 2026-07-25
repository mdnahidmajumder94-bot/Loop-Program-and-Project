user_name = "Md.Nahid Majumder"
password = "mdnahidmajumder@#94"
attempt = 0

while attempt < 3:
    user = input("Enter your username: ")
    pwd = input("Enter your password: ")

    if user == user_name and pwd == password:
        print("Welcome " + user_name + "!")
        print("You Login Successfully!")
        break

    else:
        attempt += 1
        if user != user_name and pwd != password:
            print("Invalid username and wrong password!")

        elif user != user_name:
            print("Invalid username!")

        else:
            print("Wrong Password!")

    if attempt == 3:
        print("Your account looked! ")