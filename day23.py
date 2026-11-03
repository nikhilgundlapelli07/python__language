
# Student Marks Analysis

marks = [85, 72, 90, 65, 48]

total = 0
passed = 0
failed = 0

print("STUDENT MARKS REPORT")
print("--------------------")

for i in range(len(marks)):
    print("Subject", i + 1, ":", marks[i])

    total += marks[i]

    if marks[i] >= 35:
        passed += 1
    else:
        failed += 1

average = total / len(marks)

print("--------------------")
print("Total Marks:", total)
print("Average Marks:", average)
print("Passed Subjects:", passed)
print("Failed Subjects:", failed)

for mark in marks:
    if mark >= 90:
        print(mark, "- Excellent")
    elif mark >= 75:
        print(mark, "- Very Good")
    elif mark >= 35:
        print(mark, "- Pass")
    else:
        print(mark, "- Fail")
