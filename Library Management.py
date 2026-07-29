book = ["python","java","ruby"]

print("\nWelcome to our Library")
print("1.Show book")
print("2.Borrow book")
print("3.Return book")
print("4.Exit")

while True:
    choice = int(input("Enter your choice:"))

    # print all book in library
    if choice == 1:
        for i in book:
            print(i)

    # take a book from library
    elif choice == 2:
        books = input("Enter Books Name:")
        if books in book:
            book.remove(books)
        else:
            print("Book not found")

    # return book in library
    elif choice == 3:
        re_book = input("Enter Book Name:")
        book.append(re_book)

    # Exit
    elif choice == 4:
        print("Thank you for coming our Library")
        break