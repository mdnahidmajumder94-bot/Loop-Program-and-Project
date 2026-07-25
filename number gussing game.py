import random
while True:
    lower_bound = int(input("Enter lower bound: "))
    higher_bound = int(input("Enter higher bound: "))

    secret_number = random.randint(lower_bound,higher_bound)

    for i in range(5):
        guss = int(input("Enter Guess Number: "))

        if guss == secret_number:
            print("Guess Number is Correct")
            break

        elif guss > secret_number:
            print("Guess Number is Higher Than secret Number")

        elif guss < secret_number:
            print("Guess Number is Lower Than secret Number")

