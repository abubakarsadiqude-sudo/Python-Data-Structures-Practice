# 🟢 Task 1: Student Marks Management (Basic)
# Create a Python list containing marks of 5 students.

# Example:
# marks = [85, 76, 92, 88, 79]


# Requirements:
# 1. Display all students' marks.
# 2. Add a new student's marks.
# 3. Remove a student's marks.
# 4. Update the marks of a student.
# 5. Display the total number of students.
marks = [85, 76, 92, 88, 79]
print("All Student marks" , marks)
marks.append(78)
marks.pop(2)
marks[2]=78
print("Total number of students : " , len(marks))
