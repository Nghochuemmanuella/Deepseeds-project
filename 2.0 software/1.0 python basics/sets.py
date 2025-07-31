unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "blue", "green", "yellow"}
mixed_set = {1, "hello", 3.14, True}

# Creating sets from lists (removes duplicates automatically)
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers_from_list = set(numbers_with_duplicates)

# Empty set (note: {} creates an empty dictionary, not set)
empty_set = set()

print(f"Unique numbers: {unique_numbers}")
print(f"Colors: {colors}")
print(f"From list with duplicates: {unique_numbers_from_list}")
print(f"Empty set: {empty_set}")