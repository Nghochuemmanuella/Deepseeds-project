student_info = {
    "name": "Alice Johnson",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "is_graduate": False
}


phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

# Empty dictionary
empty_dict = {}

print(f"Student info: {student_info}")
print(f"Phone book: {phone_book}")


#Accesing dictionary values
student = {
    
    "name": "Ella Blink",
    "Age": 20,
    "major": "software engineering",
    "gpa": ["python", "Calculus", "Physics"]
}
print(f"Student name: {student['name']}")
print(f"Age: {student['Age']}")
print(f"major: {student['major']}")
print(f"GPA: {student.get('gpa', 'Not available')}")
print(f"Graduation year: {student.get('grad_year', 'Not specified')}")

if "course" in student:
    print(f"current course: {student['course']}")
    
    print(f"all keys: {list(student.key())}")
    print(f"all values: {list(student.value())}")

#Dictionary Methods and operations

inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25,
    "milk": 15,
    "bread": 20
}

# Getting information about the dictionary
print(f"Number of products: {len(inventory)}")
print(f"Products: {list(inventory.keys())}")
print(f"Quantities: {list(inventory.values())}")

# Working with key-value pairs
print("Current inventory:")
for product, quantity in inventory.items():
    print(f"- {product}: {quantity}")

# Checking stock levels
low_stock_items = []
for product, quantity in inventory.items():
    if quantity < 20:
        low_stock_items.append(product)

print(f"Low stock items: {low_stock_items}")

# Copying dictionaries
backup_inventory = inventory.copy()
print(f"Backup created: {backup_inventory}")

# Clearing all items
test_dict = {"a": 1, "b": 2}
test_dict.clear()
print(f"After clearing: {test_dict}")       


#exercise in dictionary personal contact manager

contacts = {}

def add_contact(name, phone, email):
    """Add a contact to the directory."""
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"Added contact: {name}")

def update_contact(name, phone=None, email=None):
    """Update an existing contact."""
    if name in contacts:
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print(f"Updated contact: {name}")
    else:
        print(f"Contact {name} not found")

def show_all_contacts():
    """Display all contacts."""
    if not contacts:
        print("No contacts in directory")
        return

        print("Contact Directory:")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
        print()

# Test your functions
add_contact("Alice", "555-1234", "alice@email.com")
add_contact("Bob", "555-5678", "bob@email.com")
show_all_contacts()
update_contact("Alice", phone="555-9999")
show_all_contacts()

