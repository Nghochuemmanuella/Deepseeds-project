shopping_cart = ["Apples", "banana" , "Oranges", "Grapes" ]
number = [1, 2, 3, 4, 5, 6]
mixed_items = [1, 3.43, "banana" , True]
empty_cart = []
print(f"shopping cart: {shopping_cart}")
print(f"number: {number}")
print(f"mixed items: {mixed_items}")



#accessing list items
fruits = ["apple", "banana", "cherry", "elderberry"]
print(f"first fruit: {fruits[0]}")
print(f"second fruit: {fruits[1]}")
print(f"last fruit: {fruits[-1]}")
print(f"second to last: {fruits[-2]}")

print(f"first three fruits: {fruits [0:3]}")
print(f"from seconf to end: {fruits[1:]}")
print(f"every second fruit: {fruits[::2]}")

#modifying list
groceries = ["milk", "bread" ,  "eggs"]
print(f"Original list: {groceries}")

groceries.append("cheese")
print(f"After adding cheese: {groceries}")

groceries.extend(["apples", "banana"])
print(f"after adding fruits: {groceries}")

groceries.insert(1, "yogurt")
print(f"after inserting yogurt: {groceries}")

groceries[0] = "almond milk"
print(f"after changings milk: {groceries}")

groceries.remove("bread")
print(f"after removing bread: {groceries}")

removed_item = groceries.pop()
print(f"remove item: {removed_item}")
print(f"after popping: {groceries}")

specific_item = groceries.pop(1)
print(f"removed item at index 1: {specific_item}")
print(f"final list: {groceries}")