# 🟠 Task 4: Tuple Comparison and Analysis (Hard)
# Create two tuples:
# tuple1 = (10, 20, 30, 40, 50)tuple2 = (30, 40, 50, 60, 70)


# Requirements:
# 1. Find common elements between both tuples.
# 2. Find elements present in tuple1 but not in tuple2.
# 3. Find elements present in tuple2 but not in tuple1.
# 4. Combine both tuples.
# 5. Remove duplicate values from the combined result.
# 6. Display the final unique values as a tuple.

tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)
tuple1=set(tuple1)
tuple2=set(tuple2)
print("Common elements : " , tuple1.intersection(tuple2))
print("elements present in tuple1 but not in tuple2. : " , tuple1.difference(tuple2))
print("elements present in tuple2 but not in tuple1. : "  , tuple2.difference(tuple1) )
print("Combine both tuples. : " , tuple1.union(tuple2))
result = tuple1.union(tuple2)
final_result = tuple(result)
print("Final Unique Tuple:", final_result)