# 🟡 Task 5: Shopping Cart System (Medium)
# Create a shopping cart using a Python list.
# cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]


# Requirements:
# 1. Add a new product.
# 2. Remove a product.
# 3. Search for a product.
# 4. Update a product name.
# 5. Display all products.
# 6. Count total products in the cart.

cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]

new_product=input("Enter new product : ")
cart.append(new_product)
remove_product=input("Enter remove product : ")

if remove_product in cart:
    cart.remove(remove_product)
    print("After Removing:", cart)
else:
    print("Fruit not found!")
search_product=input("Enter search product : ")
if search_product in cart :
    print(search_product , "exist in the list.")
else:
    print(search_product , "does not exit in the list.")
cart[2]="Printer"
print("All products : " , cart)
print("Total items : " ,len(cart))


