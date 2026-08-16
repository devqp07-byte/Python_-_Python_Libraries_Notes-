'''Different types of error:----->'''

# Errors are problems in a program due to which the program stops execution.
# Exceptions are runtime errors that change the normal flow of the program.

'''Two types of errors occur in Python'''
# 1. Syntax Errors
# 2. Logical Errors (Exceptions)

# --------------------------------------------------

'''Syntax Error'''

# Syntax errors occur when Python grammar rules are broken.
# Syntax errors cannot be handled using try-except.

# Example of correct syntax (NO ERROR)
age = 18
if age < 18:
    print("Yes")
else:
    print("No")

# Example of syntax error (commented to avoid crash)
# if age < 18
#     print("Yes")

# --------------------------------------------------

'''Logical Errors (Exceptions)'''

# Common types of exceptions:
# 1. ZeroDivisionError
# 2. NameError
# 3. TypeError
# 4. ValueError
# 5. IndexError
# 6. KeyError
# 7. ModuleNotFoundError

# --------------------------------------------------

'''ZeroDivisionError'''
# a = 0
# print(10 / a)
# Output: ZeroDivisionError: division by zero

# --------------------------------------------------

'''NameError'''
# print(x)
# Output: NameError: name 'x' is not defined

# --------------------------------------------------

'''TypeError'''
# a = 10
# b = "20"
# total = a + b
# print(total)
# Output: TypeError: unsupported operand type(s)

# --------------------------------------------------

'''ValueError'''
# x = int("eleven")
# print(x)
# Output: ValueError: invalid literal for int()

# --------------------------------------------------

'''IndexError'''
# names = ["mohan", "sohan", "anuj", "gopal"]
# print(names[4])
# Output: IndexError: list index out of range

# --------------------------------------------------

'''KeyError'''
# user = {
#     "id": 1,
#     "name": "Tushar Sharma",
#     "age": 28
# }
# print(user["address"])
# Output: KeyError: 'address'

# --------------------------------------------------

'''ModuleNotFoundError'''
# import mathhs
# Output: ModuleNotFoundError: No module named 'mathhs'

# --------------------------------------------------

'''Exception Handling'''

# try block: tests the code for errors
# except block: handles the error
# else block: runs when no error occurs
# finally block: always executes

# --------------------------------------------------

# Example 1
print("Start Code")
try:
    data = "sample data"
    print(data)
except Exception as e:
    print(e)
print("End Code")

# --------------------------------------------------

# Example 2
print("Start Code")
def sayhi():
    print("Hello Shree!")

def saybye():
    bye = "Goodbye Shree!"
    print(bye)

try:
    sayhi()
    saybye()
except Exception as e:
    print(e)
print("End Code")

# --------------------------------------------------

# Example 3
print("Start Code")
try:
    info = "example info"
    print(info)
except Exception:
    print("An error occurred")
print("End Code")

# --------------------------------------------------

# Example 4 (TypeError handling)
print("Start Code")
try:
    i = "9"
    j = 10
    print(i + j)
except TypeError:
    print("Invalid input. Please enter numeric values.")
print("End Code")

# --------------------------------------------------

# Example 5 (try-except-else)
print("Start Code")
try:
    print("Done")
except Exception as e:
    print(e)
else:
    print("No error occurred")
print("End Code")

# --------------------------------------------------

# Example 6 (try-except-else-finally)
print("Start Code")
try:
    print("Done")
except Exception as e:
    print(e)
else:
    print("No error occurred")
finally:
    print("Always executed")
print("End Code")
