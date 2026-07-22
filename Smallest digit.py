num = 753124
smallest = 9
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num //= 10
print("Smallest number :",smallest)