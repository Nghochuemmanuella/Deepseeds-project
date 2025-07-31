point_coordinates = (10, 20)  # A point in 2D space
rgb_color = (255, 128, 0)     # Orange color values
student_record = ("Alice", 20, "Computer Science", 3.8)

# Tuples can be created without parentheses too
another_point = 5, 15
single_item_tuple = (42,)  # Note the comma - this is important!

print(f"Point coordinates: {point_coordinates}")
print(f"RGB color: {rgb_color}")
print(f"Student record: {student_record}")
print(f"Single item tuple: {single_item_tuple}")



#accessing tuple element
book_info = ("1984", "George Orwell", 1949, "Dystopian Fiction")

# Accessing individual elements
title = book_info[0]
author = book_info[1]
year = book_info[2]
genre = book_info[3]

print(f"Book: {title}")
print(f"Author: {author}")
print(f"Published: {year}")
print(f"Genre: {genre}")


title, author, year, genre = book_info
print(f"Using unpacking - Book: {title} by {author} ({year})")


first_name, last_name, *other_info = ("John", "Smith", 30, "Engineer", "New York")
print(f"Name: {first_name} {last_name}")
print(f"Other info: {other_info}")

