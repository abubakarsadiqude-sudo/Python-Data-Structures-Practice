# Task 3: Number Analysis (Basic)
# Create a list of 10 numbers.
# numbers = [12, 45, 23, 67, 89, 34, 56, 90, 11, 5]


# Requirements:
# 1. Find the largest number.
# 2. Find the smallest number.
# 3. Calculate the sum.
# 4. Calculate the average.
# 5. Count how many numbers are greater than 50.

count=int(0)
numbers = [12, 45, 23, 67, 89, 34, 56, 90, 11, 5]
print("Max = " , max(numbers))
print("Min = " , min(numbers))
print("Sum = " , sum(numbers))
print("Average = " , sum(numbers)/len(numbers))
for i in numbers:
    if i > 50:
        count=count+1
print("Number greater then 50 : " , count)
