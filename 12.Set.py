"""
===========================
PYTHON SET – DETAILED NOTES
===========================

Definition:
A set is an unordered collection of unique items.
Sets do NOT allow duplicate values.
Sets are MUTABLE.
"""

# ------------------------
# Creating Sets
# ------------------------
"""
1. Using curly brackets: {1, 2, 3}
2. Set with mixed data types
3. Empty set must use set(), not {}
"""

s1 = {10, 20, 30}
s2 = {"Python", 3.5, True}
empty_set = set()

# ------------------------
# Set Sequence (Order)
# ------------------------
"""
Sets are UNORDERED.
Items do not have fixed positions.
Indexing is NOT allowed.
"""

# ------------------------
# Accessing Set Items
# ------------------------
"""
Set items cannot be accessed by index.
Use loop to access items.
"""

for item in s1:
    print(item)

# ------------------------
# Adding Items
# ------------------------
"""
1. add() -> adds single item
2. update() -> adds multiple items
"""

s1.add(40)
s1.update([50, 60])

# ------------------------
# Removing Items
# ------------------------
"""
1. remove()   -> removes item (error if not found)
2. discard()  -> removes item (no error)
3. pop()      -> removes random item
4. clear()    -> removes all items
"""

s1.remove(20)
s1.discard(100)
s1.pop()
# s1.clear()

# ------------------------
# Copying Sets
# ------------------------
"""
1. copy() -> creates a new set
"""

new_set = s1.copy()

# ------------------------
# Looping Through Set
# ------------------------
"""
Use for loop
"""

for value in s1:
    print(value)

# ------------------------
# Joining Sets
# ------------------------
"""
1. union() -> combines sets
2. update() -> adds elements from another set
"""

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))   # {1,2,3,4,5}
a.update(b)

# ------------------------
# Set Operations
# ------------------------
"""
1. intersection() -> common items
2. difference()   -> items in one set not in other
3. symmetric_difference() -> items not common
"""

print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# ------------------------
# Checking Item in Set
# ------------------------
if 3 in a:
    print("3 is present")

# ------------------------
# Set Length
# ------------------------
print(len(a))

# ------------------------
# Nested Sets
# ------------------------
"""
Sets cannot contain other sets directly.
But they can contain tuples.
"""

nested_set = {(1, 2), (3, 4)}

# ------------------------
# Mutable vs Immutable
# ------------------------
"""
Set is MUTABLE.
frozenset is IMMUTABLE version of set.
"""

fs = frozenset([1, 2, 3])

# ------------------------
# Important Points
# ------------------------
"""
1. Sets are unordered and unindexed
2. No duplicate values allowed
3. Fast for membership testing
4. Supports mathematical operations
5. Used to remove duplicates
"""

"""
SUMMARY:
- Set = unordered, unique collection
- No indexing or slicing
- Supports union, intersection, difference
- Mutable, but frozenset is immutable
"""
