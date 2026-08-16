"""
==================================
PYTHON JUMPING STATEMENTS – NOTES
==================================

Definition:
Jumping statements are used to
change the normal flow of a loop.
"""

# ----------------------------
# Types of Jumping Statements
# ----------------------------
"""
1. break
2. continue
3. pass
"""

# ------------------------
# break Statement
# ------------------------
"""
break:
Stops the loop immediately.
Control comes out of the loop.
"""

for i in range(1, 6):
    if i == 3:
        break
    print(i)

# ------------------------
# continue Statement
# ------------------------
"""
continue:
Skips the current iteration
and moves to the next loop cycle.
"""

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# ------------------------
# pass Statement
# ------------------------
"""
pass:
Does nothing.
Used when a statement is required
but no action is needed.
"""

for i in range(1, 4):
    if i == 2:
        pass
    print(i)

# ------------------------
# Important Points
# ------------------------
"""
1. break exits the loop
2. continue skips one step
3. pass is an empty statement
4. Used only inside loops or conditions
"""

"""
SUMMARY:
- Jumping statements control loop flow
- They do not repeat code
"""

#* =================================
#*  Example of break and continue
#* =================================

for n in range(1, 8):
    if n == 3:
        continue  # skip 3
    if n == 6:
        break  # stop at 6
    print("n:", n)