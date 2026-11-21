
students = int(input("Enter number of students: "))

for i in range(1, students + 1):
    print("\nStudent", i)

    name = input("Enter student name: ")

    total = 0

    for j in range(1, 6):
        marks = int(input(f"Enter subject {j} marks: "))
        total += marks

    average = total / 5

    print("\nStudent Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)

    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")

print("\nAll student records completed!")
