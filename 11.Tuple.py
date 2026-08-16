"""
===========================
PYTHON TUPLE – DETAILED NOTES
===========================

Definition:
A tuple is an ordered collection of items.
Tuples are similar to lists but are IMMUTABLE.
This means tuple items cannot be changed.
"""

# ------------------------
# Creating Tuples
# ------------------------
"""
1. Using round brackets: (1, 2, 3)
2. Single item tuple needs comma: (5,)
3. Tuple without brackets is also allowed
"""

t1 = (10, 20, 30)
t2 = ("Python", 3.5, True)
single = (5,)

# ------------------------
# Tuple in Sequence (Order)
# ------------------------
"""
Tuples maintain order.
Items remain in the same sequence.
"""

# ------------------------
# Accessing Tuple Items
# ------------------------
"""
- Index starts from 0
- Negative index starts from -1
"""

print(t1[0])    # 10
print(t1[-1])   # 30

# ------------------------
# Tuple Slicing
# ------------------------
"""
Syntax: tuple[start:end]
"""

print(t1[0:2])  # (10, 20)
print(t1[1:])   # (20, 30)

# ------------------------
# Looping Through Tuple
# ------------------------
"""
Use for loop to access items
"""

for item in t1:
    print(item)

# ------------------------
# Tuple Methods
# ------------------------
"""
Tuple has only TWO methods:
1. count() -> counts occurrence
2. index() -> returns index of value
"""

t3 = (1, 2, 3, 2, 2)
print(t3.count(2))   # 3
print(t3.index(3))   # 2

# ------------------------
# Joining Tuples
# ------------------------
"""
Use + operator to join tuples
"""

a = (1, 2)
b = (3, 4)
c = a + b
print(c)   # (1, 2, 3, 4)

# ------------------------
# Repeating Tuples
# ------------------------
"""
Use * operator
"""

print(a * 3)   # (1,2,1,2,1,2)

# ------------------------
# Unpacking Tuples
# ------------------------
"""
Assign tuple values to variables
"""

data = ("Dev", 15, "Python")
name, age, subject = data
print(name)
print(age)
print(subject)

# ------------------------
# Updating Tuples (Indirect Way)
# ------------------------
"""
Tuples cannot be changed directly.
To update:
1. Convert tuple to list
2. Make changes
3. Convert back to tuple
"""

temp = list(t1)
temp.append(40)
t1 = tuple(temp)
print(t1)   # (10,20,30,40)

# ------------------------
# Tuple Length
# ------------------------
print(len(t1))

# ------------------------
# Checking Item in Tuple
# ------------------------
if 20 in t1:
    print("20 is present")

# ------------------------
# Nested Tuples
# ------------------------
nested = (1, (2, 3), 4)
print(nested[1])      # (2,3)
print(nested[1][0])   # 2

# ------------------------
# Mutable vs Immutable
# ------------------------
"""
Tuple is IMMUTABLE:
- Items cannot be changed
- Faster than list
- Safer for fixed data
"""

# ------------------------
# Important Points
# ------------------------
"""
1. Tuples are ordered and indexed
2. Immutable (cannot change items)
3. Faster than lists
4. Only two methods
5. Used for fixed data
"""

"""
SUMMARY:
- Tuple = ordered, immutable collection
- Supports indexing, slicing, looping
- Can be joined, unpacked, and nested
"""
