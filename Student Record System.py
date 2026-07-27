student ={}

print("\nwellcome to our school")
print("1.add student")
print("2.show student_info")
print("3.exit")

while True:
    choice = input("Enter your choice:")
    # add student in our school
    if choice == "1":
        roll = int(input("Enter Roll Number: "))
        new_student = input("Enter Student Name: ")
        Class = input("Enter Class Name: ")
        age = input("Enter Age: ")
        marks = []
        for i in range(6):
            mark = int(input(f"Enter Marks: {i + 1} : "))
            marks.append(mark)
        total = sum(marks)
        avg = total / len(marks)
        # formula to add student
        student.update({roll:{"Name":new_student,
                        "Class": Class,
                        "age":age,
                        "Grade":avg}})
    # show student info
    elif choice == "2":
        for i in student.items():
            print("Student Info : ",i)

    elif choice == "3":
        print("Exiting Program")
        break




