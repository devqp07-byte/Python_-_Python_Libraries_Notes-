# lambda function:-----> 
#A lambda function is small anonymous function that can take any number of arguments,
# but can only have one expression.

# The syntax of a lambda function is as follows:
#lambda arguments: expression 

#? basic lambda function:

name = lambda nm: nm 
print(name("john Doe"))

sum = lambda a, b: a + b
print(sum(5,10))

#lambda function inside another function:
def myfunc(n):
    return lambda a : a * n

res = myfunc(2)
print(res(11))

ress = myfunc(67)
print(ress(2))

#? lmbda function with Built-in  function:
# map(), filter(), sorted()
# 1... map()---->
numbers = [1,2,3,4,5]
squ = list(map(lambda x: x*2, numbers))
print(squ)

# 2... filter()---->
nums = [10, 15, 22, 33, 42, 55]
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)

# 3... sorted()---->
points = [(2, 3), (1, 2), (4,1), (3,4)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)

names = ["Mohan", "sohan", "ayushi", "anupam", "Zoya"]
sort_names = sorted(names, key=lambda x: x[-1]) #sort like a reverse order
# sort_names = sorted(names, key=lambda x: len(x)) # sort based on words length
print(sort_names)


'''recursion'''
# A function that calls itself is called a recursive function.

#example 1 ---->
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
        
countdown(5)

#example 2 ---->
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
result = factorial(5)
print("Factorial of 5 :  ", result)
