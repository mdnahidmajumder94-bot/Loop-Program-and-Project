# Multiplication table
num = int(input("enter a number : "))
y = 1
multi = 1

while y < num+1:
    multi *= y
    y += 1
print(multi)
