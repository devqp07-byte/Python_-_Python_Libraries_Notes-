"""
===========================
PYTHON LIST – DETAILED NOTES
===========================

Definition:
A list is an ordered collection of items.
Lists can store numbers, strings, or mixed data.
Lists are MUTABLE, which means their items can be changed.
"""

# ------------------------
# Creating Lists
# ------------------------
"""
1. Using square brackets: [1, 2, 3]
2. Empty list: []
3. Mixed data: [1, "Python", 3.5]
"""
my_list = [10, 20, 30, 40, 50]
mixed_list = [1, "Python", 3.5, True]

# ------------------------
# Accessing List Items
# ------------------------
"""
- Use index to access items (index starts from 0)
- Negative index starts from end (-1 = last item)
"""
print(my_list[0])   # 10
print(my_list[-1])  # 50

# ------------------------
# Changing List Items
# ------------------------
my_list[1] = 25    # Change 2nd item
print(my_list)     # [10, 25, 30, 40, 50]

# ------------------------
# Adding Items
# ------------------------
"""
1. append() -> adds item at end
2. insert() -> adds item at specific position
3. extend() -> adds multiple items
"""
my_list.append(60)            # [10, 25, 30, 40, 50, 60]
my_list.insert(2, 28)         # [10, 25, 28, 30, 40, 50, 60]
my_list.extend([70, 80])      # [10, 25, 28, 30, 40, 50, 60, 70, 80]

# ------------------------
# Removing Items
# ------------------------
"""
1. remove() -> removes first occurrence of value
2. pop()    -> removes item by index
3. clear()  -> removes all items
"""
my_list.remove(28)    # remove value 28
my_list.pop(2)        # remove 3rd item (index 2)
# my_list.clear()     # empties the list

# ------------------------
# Copying Lists
# ------------------------
"""
1. copy() -> shallow copy
2. list() -> create new list from existing
"""
new_list = my_list.copy()
another_list = list(my_list)

# ------------------------
# Sorting Lists
# ------------------------
"""
1. sort()    -> sorts list in ascending order
2. reverse() -> reverses list
"""
numbers = [50, 10, 70, 30]
numbers.sort()        # [10, 30, 50, 70]
numbers.reverse()     # [70, 50, 30, 10]

# ------------------------
# Looping Through Lists
# ------------------------
"""
Use for loop to access each item
"""
for item in my_list:
    print(item)

# ------------------------
# List Length
# ------------------------
print(len(my_list))   # Number of items

# ------------------------
# Nested Lists
# ------------------------
nested_list = [1, [2, 3], 4]
print(nested_list[1])      # [2,3]
print(nested_list[1][0])   # 2

# ------------------------
# List Slicing
# ------------------------
"""
Get a part of the list using slicing
Syntax: list[start:end]
- Includes start index, excludes end index
"""
print(my_list[1:4])   # 2nd to 4th item
print(my_list[:3])    # first 3 items
print(my_list[3:])    # from 4th to last

# ------------------------
# Checking Item in List
# ------------------------
if 50 in my_list:
    print("50 is present")
else:
    print("50 not found")

# ------------------------
# Important Points
# ------------------------
"""
1. Lists are ordered and indexed
2. Mutable → items can be changed
3. Can contain duplicate items
4. Supports all operations like add, remove, sort, copy
5. Can loop through list
6. Nested lists are possible
"""

"""
SUMMARY:
- List = ordered, mutable collection of items
- Can store numbers, strings, mixed data, or other lists
- Supports indexing, slicing, adding, removing, sorting, copying, looping
"""
