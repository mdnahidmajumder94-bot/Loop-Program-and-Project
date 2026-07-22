num = int(input("enter the number: "))
product = 1
while num > 0:
    digit = num % 10
    product *= digit
    num //= 10
print("digit of product = ",product)