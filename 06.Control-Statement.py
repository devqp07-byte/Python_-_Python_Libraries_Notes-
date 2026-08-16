"""
==================================
PYTHON CONTROL STATEMENT – NOTES
==================================

Definition:
Control statements are used to control
the flow of a program.
They help the program take decisions.
"""

# ------------------------
# if Statement
# ------------------------
"""
if statement:
The if statement checks a condition.
If the condition is True,
the code inside if runs.
"""

# ------------------------
# if-else Statement
# ------------------------
"""
if-else statement:
If the condition is True,
if block runs.
If the condition is False,
else block runs.
"""

# ------------------------
# if-elif-else Statement
# ------------------------
"""
if-elif-else statement:
Used to check more than one condition.
The first True condition runs.
Only one block executes.
"""

# ------------------------
# Nested if Statement
# ------------------------
"""
nested if statement:
An if statement inside another if.
Used when one condition depends on another.
"""

# -----------------------------
# Example 1: Simple Calculator
# -----------------------------
"""
Performs calculation based on user choice.
"""

num1 = 10
num2 = 5
choice = "+"

if choice == "+":
    print(num1 + num2)
elif choice == "-":
    print(num1 - num2)
elif choice == "*":
    print(num1 * num2)
elif choice == "/":
    print(num1 / num2)
else:
    print("Invalid choice")

# --------------------------------------------------
# Example 2: Greeting Based on Indian Time (AM / PM)
# --------------------------------------------------
"""
Indian Time Rules:
Morning   : 5 AM  – 11:59 AM
Afternoon : 12 PM – 3:59 PM
Evening   : 4 PM  – 7:59 PM
Night     : 8 PM  – 4:59 AM
"""

hour = 7          
period = "PM"     

if period == "AM":
    if hour >= 5 and hour <= 11:
        print("Good Morning")
    else:
        print("Good Night")

elif period == "PM":
    if hour == 12 or hour <= 3:
        print("Good Afternoon")
    elif hour >= 4 and hour <= 7:
        print("Good Evening")
    else:
        print("Good Night")

#---------------------------
# Example 3: Printing week 
#---------------------------

week = int(input("Enter a number between 1 and 7: "))    
if week == 1:
     print("Monday")
elif week == 2:
     print("Tuesday")
elif week == 3:
     print("Wednesday")
elif week == 4:
     print("Thursday")
elif week == 5:
     print("Friday")
elif week == 6:
     print("Saturday")
elif week == 7:
     print("Sunday")
else:
    print("Invalid input! please enter a valid number between 1 to 7")

#-------------------
# Import Calendar
#-------------------

import calendar
month = 9
year = 2026
# Display calendar
print(calendar.month(year, month))

#-----------------------------
# Makeing Calculator
#----------------------------
num1 = int(input("Enter first number: "))
operation = input("Enter your operation: ")  
num2 = int(input("Enter second number: "))

op = "+","-","/","*","**"

if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2)
elif operation == "**":
    print(num1 ** num2)

else:
    print("Enter right values")


# --------------------------
# Important Points
# --------------------------
"""
1. Conditions give True or False
2. Indentation is mandatory in Python
3. if starts decision making
4. else is optional
"""

"""
SUMMARY:
- Control statements make decisions
- Used to run code based on conditions
- Useful in real-life programs
"""

