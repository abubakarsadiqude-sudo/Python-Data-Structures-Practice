# 🟡 Task 3: Even and Odd Numbers (Intermediate)
# Create a tuple containing 10 integers.

# Example:
# numbers = (12, 15, 20, 23, 30, 35, 40, 45, 50, 55)


# Requirements:
# 1. Separate even and odd numbers.
# 2. Store even numbers in a separate list.
# 3. Store odd numbers in another list.
# 4. Count total even numbers.
# 5. Count total odd numbers.
# 6. Calculate the sum of even numbers.
# 7. Calculate the sum of odd numbers.
even=[]
odd=[]
count_even=0
count_odd=0

numbers = (12, 15, 20, 23, 30, 35, 40, 45, 50, 55)
for i in numbers:
    if i % 2 == 0:
        even.append(i)
        count_even += 1
    else:
        odd.append(i)
        count_odd += 1
print("Even number : " , even)
print("Odd number : " , odd)
print("Number of even number : " , count_even)
print("Number of odd number : " ,count_odd)
print("Sum of even numbers : " , sum(even))
print("Sum of odd numbers : " , sum(odd))
        
