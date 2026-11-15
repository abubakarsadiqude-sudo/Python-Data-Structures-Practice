# 🟢 Task 2: Favorite Fruits List (Basic)
# Create a list containing 5 favorite fruits.

# Requirements:
# 1. Display all fruits.
# 2. Add a new fruit.
# 3. Remove a fruit.
# 4. Check whether a particular fruit exists.
# 5. Display the first and last fruit.
fruits = []


for i in range(5):
    name = input("Enter the name of fruit: ")
    fruits.append(name)

print("All fruits:", fruits)


new_fruit = input("Enter new fruit: ")
fruits.append(new_fruit)

print("After Adding:", fruits)


remove_fruit = input("Enter fruit to remove: ")

if remove_fruit in fruits:
    fruits.remove(remove_fruit)
    print("After Removing:", fruits)
else:
    print("Fruit not found!")

search_fruit = input("Enter fruit to search: ")

if search_fruit in fruits:
    print(search_fruit, "exists in the list.")
else:
    print(search_fruit, "does not exist in the list.")

print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])