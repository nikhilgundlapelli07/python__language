
# Student Grade Management System

print("=" * 45)
print("       STUDENT GRADE MANAGEMENT SYSTEM")
print("=" * 45)

# Student details
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# Taking subject marks
python = float(input("Enter Python marks: "))
java = float(input("Enter Java marks: "))
mysql = float(input("Enter MySQL marks: "))
aptitude = float(input("Enter Aptitude marks: "))
communication = float(input("Enter Communication marks: "))

# Calculating total and percentage
total = python + java + mysql + aptitude + communication
percentage = total / 5

print("\n" + "=" * 45)
print("             STUDENT REPORT")
print("=" * 45)

print("Student Name:", name)
print("Roll Number:", roll_number)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

# Checking valid marks
if any(mark < 0 or mark > 100 for mark in
       [python, java, mysql, aptitude, communication]):
    print("Invalid marks! Enter marks between 0 and 100.")

else:
    # Checking pass or fail
    if (python >= 35 and java >= 35 and
        mysql >= 35 and aptitude >= 35 and
        communication >= 35):

        print("Result: PASS")

        # Grade calculation
        if percentage >= 90:
            print("Grade: A+")
            print("Performance: Excellent")

        elif percentage >= 80:
            print("Grade: A")
            print("Performance: Very Good")

        elif percentage >= 70:
            print("Grade: B")
            print("Performance: Good")

        elif percentage >= 60:
            print("Grade: C")
            print("Performance: Average")

        elif percentage >= 50:
            print("Grade: D")
            print("Performance: Satisfactory")

        else:
            print("Grade: E")
            print("Performance: Needs Improvement")

    else:
        print("Result: FAIL")
        print("Grade: F")
        print("Performance: Work Hard")

print("=" * 45)
print("       THANK YOU!")
print("=" * 45)
