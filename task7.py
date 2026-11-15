# 🟢 Task 2: Tuple Operations (Basic)
# Create a tuple containing 10 integers.

# Example:
# numbers = (10, 20, 30, 40, 50, 10, 20, 60, 70, 80)


# Requirements:
# 1. Display all numbers.
# 2. Find the length of the tuple.
# 3. Count how many times 10 appears.
# 4. Find the index of 50.
# 5. Check whether 100 exists in the tuple.
# 6. Display the first five elements.

numbers = (10, 20, 30, 40, 50, 10, 20, 60, 70, 80)
print( "Tuple : ",numbers)
print("Length of Tuple : ",len(numbers))
print("10 appears" , numbers.count(10),"Times")
print("Index of 50 " , numbers.index(50))

if 100 in numbers:
    print("100 exit in the tuple.")
else:
    print("100 does not exit in the list.")
print("First five elements ",numbers[:5])
