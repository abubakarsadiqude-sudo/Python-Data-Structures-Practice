# 🔴 Task 5: University Student Result Management (Very Hard)
# Create a university student result management system using nested tuples.

# Example:
# students = (    ("Ali", 101, (85, 90, 88)),    ("Ahmed", 102, (75, 80, 85)),    ("Abubakar", 103, (90, 95, 92)))


# Requirements:
# 1. Display all student records.
# 2. Display each student's name and roll number.
# 3. Calculate the total marks of each student.
# 4. Calculate the average marks of each student.
# 5. Find the student with the highest average.
# 6. Display students who scored an average above 80.
# 7. Display the overall class average.

students = (
    ("Ali", 101, (85, 90, 88)),
    ("Ahmed", 102, (75, 80, 85)),
    ("Abubakar", 103, (90, 95, 92))
)

# Variables
total_class_marks = 0
total_students = len(students)

highest_average = 0
top_student = ""

# 1. Display all student records
print("\n========== ALL STUDENT RECORDS ==========")

for student in students:
    print(student)


# 2, 3, 4. Display name, roll number, total and average
print("\n========== STUDENT RESULTS ==========")

for student in students:

    name = student[0]
    roll_no = student[1]
    marks = student[2]

    total = sum(marks)
    average = total / len(marks)

    total_class_marks += total

    print("\nName:", name)
    print("Roll Number:", roll_no)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", average)

    # 5. Find student with highest average
    if average > highest_average:
        highest_average = average
        top_student = name


# 5. Display highest average student
print("\n========== TOP STUDENT ==========")

print("Student Name:", top_student)
print("Highest Average:", highest_average)


# 6. Students with average above 80
print("\n========== STUDENTS ABOVE 80 AVERAGE ==========")

for student in students:

    name = student[0]
    marks = student[2]

    average = sum(marks) / len(marks)

    if average > 80:
        print(name, ":", average)



overall_average = total_class_marks / (total_students * 3)

print("\n========== CLASS RESULT ==========")

print("Overall Class Average:", overall_average)