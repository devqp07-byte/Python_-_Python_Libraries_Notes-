"""
===========================
PYTHON FUNCTIONS – NOTES
===========================

Definition:
A function is a block of code that
performs a specific task.
It runs only when it is called.
"""

# ------------------------
# Why Functions are Used
# ------------------------
"""
1. To reuse code
2. To reduce repetition
3. To make program clean and readable
4. To divide big problems into small parts
5. Easier to Debug
"""

# ------------------------
# Parts of a Function
# ------------------------
"""
A function contains:
1. def keyword
2. Function name
3. Parameters (optional)
4. Function body (indented code)
"""

# ------------------------
# Syntax of Function
# ------------------------
"""
def function_name(parameters):
    function body
"""

# ------------------------
# Simple Function (No Parameter)
# ------------------------
def greet():
    print("Hello, Welcome to Python")

greet()

# ------------------------
# Function with Parameters
# ------------------------
def add(a, b):
    print(a + b)

add(5, 3)

# ------------------------
# Function with Return Value
# ------------------------
def square(num):
    return num * num

result = square(4)
print(result)

# ------------------------
# Difference: print vs return
# ------------------------
"""
print() -> shows output
return  -> sends value back
"""

# ------------------------
# Default Parameter Function
# ------------------------
def welcome(name="User"):
    print("Welcome", name)

welcome()
welcome("Dev")

# ------------------------
# Types of Functions
# ------------------------
"""
1. Built-in Functions
   Examples: print(), len(), type(), input()

2. User-defined Functions
   Created by programmer using def
"""

# ------------------------
# Calling a Function
# ------------------------
"""
Function runs only when called
"""

# ------------------------
# Variable Scope
# ------------------------
"""
Variables inside function are LOCAL
Variables outside function are GLOBAL
"""

# ------------------------
# pass Statement in Function
# ------------------------
"""
Used when function is empty
"""

def test():
    pass

# ------------------------
# Important Points
# ------------------------
"""
1. Function name should be meaningful
2. Indentation is mandatory
3. Function can be reused many times
4. return stops function execution
"""

"""
SUMMARY:
- Function is a reusable block of code
- Defined using def keyword
- Can take parameters
- Can return values
"""




