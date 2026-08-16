"""
===========================
PYTHON LOOPS – NOTES
===========================

Definition:
Loops are used to repeat a block of code
again and again.
They save time and reduce code length.
"""

# ------------------------
# Types of Loops in Python
# ------------------------
"""
1. for loop
2. while loop
"""

# ------------------------
# for Loop
# ------------------------
"""
for loop:
Used when the number of repetitions
is already known.

Mostly used with range().
"""

for i in range(1, 6):
    print(i)

# ------------------------
# while Loop
# ------------------------
"""
while loop:
Used when the number of repetitions
is not known.

It runs as long as the condition is True.
"""

i = 1
while i <= 5:
    print(i)
    i = i + 1
    
# ------------------------------------
#  Differences between for and range
# ------------------------------------

"""
for = the loop (it repeats code)
range = a tool that makes numbers for the loop to use
"""


''' ------------------------
    Important Points
    ------------------------
'''
# 1. Loops repeat code automatically
# 2. for loop is easy and common
# 3. while loop depends on condition
# 4. Indentation is very important


"""
SUMMARY:
- Loops are used for repetition
- for → fixed number of times
- while → condition based
"""


"""
==========================
    For Loop Practice
==========================
"""

#! Example 1: for + range
for i in range(3):
    print(i)  # prints 0, 1, 2

#? Example 2: for WITHOUT range
for item in ["a", "b", "c"]:
    print(item)

#! Example 3: another range example
for i in range(1, 4):
    print("from 1 to 3:", i)

#? Example 4: range with step (multiples of 5)
for i in range(5, 31, 5):
    print("multiple of 5:", i)

#! Example 5: counting down
for i in range(5, 0, -1):
    print("countdown:", i)

#? Example 6: loop through a string
for ch in "python":
    print("letter:", ch)

#! Example 7: loop with index using enumerate
names = ["Ali", "Sara", "Tom"]
for idx, name in enumerate(names, start=1):
    print("name", idx, "=", name)

#? Example 8: sum numbers using a loop
total = 0
for n in range(1, 6):
    total += n
print("sum 1..5 =", total)

#! Example 10: nested loops (small table)
for row in range(1, 4):
    for col in range(1, 4):
        print(row, "x", col, "=", row * col)

#? Example 11: To find out odd numbers

odd = [x for x in range(1, 1000) if x % 2 != 0]       
print(odd)

#! Example 12: Figuring out even nums from given list

even = [1,22,43,56,87,88]
for e in even:
    if e % 2 == 0:
        print(e)

#? Example 13: Printing table

for i in range(51,511,51):
    print(i)

#! Example 14: Printing squares 

square = [x * x for x in range(1,101)]
print(square)

#? Example 15: Finding squares using for loop 

for i in range(1, 21):
    print(i,- i*i)

#! Example 16: Finding cube using for loop 

for i in range(1, 21):
    print(i,- i*i*i)

#? Example 17: Printing table of your own choice

Table = int(input("Enter a number: "))
for Tbl in range(1,11):
    print(Table * Tbl)

#! Example 18: Finding total of a given list 

nums = [3,6,9,12,15]
total = 0 
for i in nums:
    total += i
print(total)

#? Example 19: printing '*' using 'for' loop

for i in range(1, 6):
    print("*" * i)

#! Example 20: printing numbers in horizontal line

for i in range(1, 6):
    print(i, end=" ")

#? Example 21: printing full table including main value 

for i in range(1,11):
    print("7 *", i, "=", 7 * i)

#! Example 21: Counting how many numbers between 1 and 

count = 0 

for i in range(1,51):
    if i % 5 == 0:
        count = count + 1
    
print("Count =", count)