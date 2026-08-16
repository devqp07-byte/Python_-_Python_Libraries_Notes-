"""
================================
PYTHON STRINGS – DETAILED NOTES
================================

Definition:
A string is a sequence of characters.
Strings are used to store text in Python.
"""

# ------------------------
# Creating Strings
# ------------------------
"""
Strings can be created using:
1. Single quotes: 'Hello'
2. Double quotes: "Hello"
3. Triple quotes (for multi-line text): '''Hello'''
"""


# ------------------------
# String Indexing
# ------------------------
"""
Each character in a string has an index number.
- Index starts from 0
- Last character index = length-1
- Negative indexing: -1 is last character
"""

text = 'Python'
# P -> index 0, y -> 1, n -> 5
# Negative: n -> -1, o -> -2

# ------------------------
# String Slicing
# ------------------------
"""
Slicing is used to get a part of the string.
Syntax: string[start:end]
- Includes start index
- Excludes end index
"""

name = "Python"
# name[0:4] -> 'Pyth'

# ------------------------
# Concatenation
# ------------------------
"""
1. Concatenation (+)   -> Join strings
2. Repetition (*)      -> Repeat strings
3. Length (len())      -> Get number of characters
"""

# ------------------------
# Modify String Methods
# ------------------------
"""
1. upper()    -> Converts to uppercase
2. lower()    -> Converts to lowercase
3. strip()    -> Removes extra spaces
4. replace()  -> Replaces text
5. split()    -> Splits string into list
6. find()     -> Finds first occurrence
"""

# ------------------------
# Mutable or Immutable
# ------------------------
"""
Strings are IMMUTABLE:
- You cannot change characters directly
- You can create a new string instead
"""

# ------------------------
# Escape Characters
# ------------------------
"""
Special characters in strings:
\n -> New line
\t -> Tab space
\\ -> Backslash
\' -> Single quote
\" -> Double quote
"""

# ------------------------
# f-Strings (String Formatting)
# ------------------------
"""
Used to insert variables into strings easily
"""

name = "Dev"
age = 15
print(f"My name is {name} and I am {age} years old")

# ------------------------
# Important Points
# ------------------------
"""
1. Strings store text
2. Indexed & sliced
3. Immutable
4. Use methods for text operations
5. Can use +, *, len(), f-string
"""

"""
SUMMARY:
- String = sequence of characters
- Supports indexing, slicing, concatenation
- Immutable but easy to manipulate
"""
