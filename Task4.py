# 🟡 Task 4: Even and Odd Numbers (Medium)
# Create a list of 15 numbers.

# Requirements:
# 1. Separate even numbers into another list.
# 2. Separate odd numbers into another list.
# 3. Display both lists.
# 4. Count even and odd numbers.
# 5. Calculate the sum of even numbers.

numbers = []
even_numbers = []
odd_numbers = []

count_even = 0
count_odd = 0
sum_even = 0


for i in range(15):
    number = int(input("Enter a number: "))
    numbers.append(number)


for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
        sum_even += i
        count_even += 1
    else:
        odd_numbers.append(i)
        count_odd += 1


print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

print("How many even numbers:", count_even)
print("How many odd numbers:", count_odd)

print("Sum of even numbers:", sum_even)


