# pattern 1
row = int(input("enter the rows number: "))
for i in range(1,row+1):
    print("*" * i)

# pyramid pattern
rows = int(input("enter the rows number: "))
for j in range(1,rows+1):
    print(" " * (rows-j) + "*" * (2 * j -1))

# diamond pattern
rowes = int(input("enter the rows number: "))
for m in range(1,rowes+1):
    print(" " * (rows - m) + "*" * (2 * m - 1))
for n in range(rows,0,-1):
    print(" " * (rows - n) + "*" * (2 * n - 1))

