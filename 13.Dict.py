"""
===========================
PYTHON DICTIONARY (dict) – DETAILED NOTES
===========================

Definition:
A dictionary is a collection of data stored
in KEY : VALUE pairs.

- Keys are UNIQUE
- Values can be duplicated
- Dictionary is MUTABLE
"""

# ------------------------
# Creating Dictionary
# ------------------------
"""
1. Using curly brackets {}
2. Each item is written as key : value
"""

student = {
    "name": "Dev",
    "age": 15,
    "course": "Python"
}

empty_dict = {}

# ------------------------
# Dictionary Order
# ------------------------
"""
Dictionaries are ORDERED (Python 3.7+).
Items maintain insertion order.
"""

# ------------------------
# Accessing Dictionary Items
# ------------------------
"""
Access values using keys
"""

print(student["name"])
print(student.get("age"))

# ------------------------
# Changing / Updating Values
# ------------------------
"""
Change value using key
"""

student["age"] = 16
print(student)

# ------------------------
# Adding New Items
# ------------------------
"""
Add new key-value pair
"""

student["city"] = "Delhi"

# ------------------------
# Removing Items
# ------------------------
"""
1. pop()    -> removes specific key
2. popitem() -> removes last item
3. del      -> deletes key
4. clear()  -> removes all items
"""

student.pop("city")
# student.popitem()
# del student["age"]
# student.clear()

# ------------------------
# Dictionary Methods
# ------------------------
"""
Common dictionary methods:
"""

keys = student.keys()       # all keys
values = student.values()   # all values
items = student.items()     # key-value pairs

# ------------------------
# Looping Through Dictionary
# ------------------------
"""
Loop through keys, values, or items
"""

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)

# ------------------------
# Copying Dictionary
# ------------------------
"""
1. copy() -> creates new dictionary
"""

new_student = student.copy()

# ------------------------
# Nested Dictionary
# ------------------------
"""
Dictionary inside another dictionary
"""

school = {
    "student1": {"name": "Dev", "age": 15},
    "student2": {"name": "Aman", "age": 16}
}

print(school["student1"]["name"])

# ------------------------
# Checking Key in Dictionary
# ------------------------
if "name" in student:
    print("Key exists")

# ------------------------
# Dictionary Length
# ------------------------
print(len(student))

# ------------------------
# Mutable vs Immutable
# ------------------------
"""
Dictionary is MUTABLE:
- Values can be changed
- Keys must be IMMUTABLE
  (int, string, tuple allowed)
"""

# ------------------------
# Real-Life Use of Dictionary
# ------------------------
"""
1. Student records
2. Login systems (username : password)
3. Phone directory
4. JSON data handling
"""

# ------------------------
# Important Rules
# ------------------------
"""
1. Keys must be unique
2. Keys cannot be list or set
3. Values can be any data type
4. Fast data access using keys
"""

"""
SUMMARY:
- Dictionary stores data as key:value
- Ordered, mutable, and fast
- Used for structured data
"""
