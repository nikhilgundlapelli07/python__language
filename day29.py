
# ==========================================
# STUDENT MANAGEMENT SYSTEM
# Python Project Based on Loops
# ==========================================

students = []

subjects = ["Python", "DSA", "SQL", "English"]


# Function to get valid marks
def get_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter numbers only.")


# Function to add student
def add_student():
    print("\n--- ADD STUDENT ---")

    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter student name: ")

    marks = {}

    for subject in subjects:
        marks[subject] = get_marks(subject)

    total = 0

    for mark in marks.values():
        total += mark

    average = total / len(subjects)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    result = "Pass"

    for mark in marks.values():
        if mark < 35:
            result = "Fail"
            break

    student = {
        "id": student_id,
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }

    students.append(student)

    print("\nStudent added successfully!")


# Function to display all students
def display_students():
    print("\n--- ALL STUDENTS ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\n-------------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])

        for subject, mark in student["marks"].items():
            print(subject, ":", mark)

        print("Total:", student["total"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
        print("Result:", student["result"])


# Function to search student
def search_student():
    print("\n--- SEARCH STUDENT ---")

    search_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Total:", student["total"])
            print("Average:", student["average"])
            print("Grade:", student["grade"])
            print("Result:", student["result"])
            return

    print("Student not found!")


# Function to display passed students
def pass_students():
    print("\n--- PASSED STUDENTS ---")

    count = 0

    for student in students:
        if student["result"] == "Pass":
            print(student["name"], "-", student["average"])
            count += 1

    if count == 0:
        print("No passed students found.")

    print("Total passed students:", count)


# Function to display failed students
def fail_students():
    print("\n--- FAILED STUDENTS ---")

    count = 0

    for student in students:
        if student["result"] == "Fail":
            print(student["name"], "-", student["average"])
            count += 1

    if count == 0:
        print("No failed students found.")

    print("Total failed students:", count)


# Function to find class topper
def class_topper():
    print("\n--- CLASS TOPPER ---")

    if not students:
        print("No student records found.")
        return

    topper = students[0]

    for student in students:
        if student["average"] > topper["average"]:
            topper = student

    print("Topper Name:", topper["name"])
    print("Student ID:", topper["id"])
    print("Average:", round(topper["average"], 2))


# Function to display grade-wise students
def grade_report():
    print("\n--- GRADE-WISE REPORT ---")

    grades = ["A+", "A", "B", "C", "D", "F"]

    for grade in grades:
        print("\nGrade:", grade)

        count = 0

        for student in students:
            if student["grade"] == grade:
                print(student["name"])
                count += 1

        print("Total:", count)


# Function to delete student
def delete_student():
    print("\n--- DELETE STUDENT ---")

    delete_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# Function to generate class report
def class_report():
    print("\n--- COMPLETE CLASS REPORT ---")

    if not students:
        print("No student records available.")
        return

    total_students = len(students)
    total_marks = 0
    passed = 0
    failed = 0

    for student in students:
        total_marks += student["average"]

        if student["result"] == "Pass":
            passed += 1
        else:
            failed += 1

    class_average = total_marks / total_students

    print("Total Students:", total_students)
    print("Passed Students:", passed)
    print("Failed Students:", failed)
    print("Class Average:", round(class_average, 2))

    class_topper()


# Main menu
while True:

    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Passed Students")
    print("5. Failed Students")
    print("6. Class Topper")
    print("7. Grade-Wise Report")
    print("8. Delete Student")
    print("9. Complete Class Report")
    print("10. Exit")

    choice = input("\nEnter your choice (1-10): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        pass_students()

    elif choice == "5":
        fail_students()

    elif choice == "6":
        class_topper()

    elif choice == "7":
        grade_report()

    elif choice == "8":
        delete_student()

    elif choice == "9":
        class_report()

    elif choice == "10":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please select 1-10.")
