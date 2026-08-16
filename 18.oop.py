# WHAT IS OOP?
# OOP stands for Object-Oriented Programming.

# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

# ADVANTAGES OF OOPS:
#     * Provides a clear structure to programs.
#     * Makes code easier to maintain, reuse and debug.
#     * Helps keeps your code DRY (don't repeat yourself).
#     * Allows you to build reusable applications with less code.
    
# NOTE:- The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.
        
# WHAT ARE CLASSES AND OBJECTS?
# Classes and Objects are the two core concepts in object-oriented programming.
# A class defines what an object should look like, and an object is created based on that class.


#! Class and Object :-
"""
    * Everything in Python is an object. An object has a state and behaviors.
    * To create an object, you define a class first.
    * And then, from the class, you can create one or more objects.
    * The objects are instances of a class.
"""

# define a class:
# To define a class, you use the class keyword followed by the class name.
""" class Person:
    pass """

# create an object:
# To create an object from a class, you use the class name followed by the object name.
""" user1 = Person()
user2 = Person() """

#? examples:---->>
class Person:
    name = "Tushar Sharma"
    age = 29
    city = "Agra"
    
    def info(self):
        return f"My name is {self.name}. I am {self.age} years old. I am living in {self.city}."
    
user1 = Person()
data = user1.info()
print(data)

user2 = Person()
user2.name = "Ayushi Jain"
user2.age = 26
user2.city = "New Delhi"
data = user2.info()
print(data)

user3 = Person()
data = user3.info()
print(data)


# ============================================
# COMPLETE OBJECT-ORIENTED PROGRAMMING (OOP) GUIDE
# ============================================

print("\n" + "=" * 60)
print("OBJECT-ORIENTED PROGRAMMING - FULL TOPIC EXPLANATION")
print("=" * 60)

# ============================================
# 1. CLASS AND OBJECTS
# ============================================
print("\n" + "=" * 60)
print("1. CLASSES AND OBJECTS")
print("=" * 60)
print("""
CLASS: A blueprint/template for creating objects
OBJECT: An instance of a class

Example: Class is like a car design, Object is the actual car
""")
# =====================
# 1. CLASS AND OBJECTS
# =====================
class Car:
    """A simple car class"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating objects (instances)
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

print("=" * 50)
print("1. CLASS AND OBJECTS")
print("=" * 50)
print(car1.display_info())
print(car2.display_info())


# 2. CONSTRUCTOR (__init__)
# =========================
class Student:
    """Student class with constructor"""
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

print("\n" + "=" * 50)
print("2. CONSTRUCTOR (__init__)")
print("=" * 50)
student1 = Student("Alice", 101, 95)
student2 = Student("Bob", 102, 87)
student1.display()
student2.display()


# 3. SELF PARAMETER
# ================
class Person3:
    """Person class to demonstrate self"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

print("\n" + "=" * 50)
print("3. SELF PARAMETER")
print("=" * 50)
person1 = Person3("John", 30)
person1.greet()


# 4. INHERITANCE (Single Inheritance)
# ===================================
class Animal:
    """Parent class"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    """Child class inheriting from Animal"""
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    """Another child class"""
    def speak(self):
        return f"{self.name} meows"

print("\n" + "=" * 50)
print("4. INHERITANCE")
print("=" * 50)
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())


# 5. MULTILEVEL INHERITANCE
# ==========================
class Vehicle:
    """Base class"""
    def __init__(self, brand):
        self.brand = brand
    
    def display(self):
        return f"Brand: {self.brand}"

class Car2(Vehicle):
    """Intermediate class"""
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class ElectricCar(Car2):
    """Final derived class"""
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery
    
    def display(self):
        return f"Brand: {self.brand}, Model: {self.model}, Battery: {self.battery}kWh"

print("\n" + "=" * 50)
print("5. MULTILEVEL INHERITANCE")
print("=" * 50)
electric_car = ElectricCar("Tesla", "Model S", 100)
print(electric_car.display())


# 6. MULTIPLE INHERITANCE
# =======================
class Flyer:
    """Mixin class for flying"""
    def fly(self):
        return "Flying in the sky!"

class Swimmer:
    """Mixin class for swimming"""
    def swim(self):
        return "Swimming in water!"

class Duck(Flyer, Swimmer):
    """Duck class inheriting from multiple classes"""
    def quack(self):
        return "Quack! Quack!"

print("\n" + "=" * 50)
print("6. MULTIPLE INHERITANCE")
print("=" * 50)
duck = Duck()
print(duck.fly())
print(duck.swim())
print(duck.quack())


# 7. ENCAPSULATION (Data Hiding)
# ==============================
class BankAccount:
    """Bank account with encapsulation"""
    def j__init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance or invalid amount")
    
    def get_balance(self):
        return self.__balance

print("\n" + "=" * 50)
print("7. ENCAPSULATION (Data Hiding)")
print("=" * 50)
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current Balance: ${account.get_balance()}")


# 8. POLYMORPHISM (Method Overriding)
# ===================================
class Shape:
    """Base class"""
    def area(self):
        pass

class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    """Circle class"""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

print("\n" + "=" * 50)
print("8. POLYMORPHISM (Method Overriding)")
print("=" * 50)
shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(f"Area: {shape.area()}")


# 9. ABSTRACTION (Using ABC - Abstract Base Class)
# ================================================
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    """Abstract base class"""
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass


class MySQLConnection(DatabaseConnection):
    """MySQL implementation"""
    def connect(self):
        return "Connected to MySQL Database"
    
    def execute_query(self, query):
        return f"Executing MySQL query: {query}"

class MongoConnection(DatabaseConnection):
    """MongoDB implementation"""
    def connect(self):
        return "Connected to MongoDB"
    
    def execute_query(self, query):
        return f"Executing MongoDB query: {query}"

print("\n" + "=" * 50)
print("9. ABSTRACTION (Abstract Base Classes)")
print("=" * 50)
mysql = MySQLConnection()
print(mysql.connect())
print(mysql.execute_query("SELECT * FROM users"))

mongo = MongoConnection()
print(mongo.connect())
print(mongo.execute_query("db.users.find()"))


# 10. STATIC METHODS AND CLASS METHODS
# ===================================
class MathOperations:
    """Class with static and class methods"""
    pi = 3.14
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius * radius
    
    def multiply(self, a, b):
        return a * b

print("\n" + "=" * 50)
print("10. STATIC AND CLASS METHODS")
print("=" * 50)
print(f"Static method (add): {MathOperations.add(10, 5)}")
print(f"Class method (circle_area): {MathOperations.circle_area(5)}")

math_obj = MathOperations()
print(f"Instance method (multiply): {math_obj.multiply(4, 7)}")


# 11. PROPERTIES (Getters and Setters)
# ===================================
class Temperature:
    """Temperature class with properties"""
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

print("\n" + "=" * 50)
print("11. PROPERTIES (Getters and Setters)")
print("=" * 50)
temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
temp.celsius = 30
print(f"New Celsius: {temp.celsius}°C")


# 12. DUNDER METHODS (Magic Methods)
# ==================================
class Book:
    """Book class with dunder methods"""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

print("\n" + "=" * 50)
print("12. DUNDER METHODS (Magic Methods)")
print("=" * 50)
book1 = Book("Python Guide", "John Doe", 300)
book2 = Book("Java Guide", "Jane Doe", 400)

print(str(book1))  # Uses __str__
print(repr(book1))  # Uses __repr__
print(f"Pages: {len(book1)}")  # Uses __len__
print(f"book1 < book2: {book1 < book2}")  # Uses __lt__


# 13. PRACTICAL EXAMPLE: COMPLETE SYSTEM
# ======================================
class Employee:
    """Employee class with inheritance"""
    employee_count = 0
    
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self._salary = salary
        Employee.employee_count += 1
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value
    
    def display_info(self):
        return f"Name: {self.name}, Department: {self.department}, Salary: ${self._salary}"
    
    @classmethod
    def total_employees(cls):
        return cls.employee_count


class Manager(Employee):
    """Manager class inheriting from Employee"""
    def __init__(self, name, department, salary, team_size):
        super().__init__(name, department, salary)
        self.team_size = team_size
    
    def display_info(self):
        return f"Manager - Name: {self.name}, Department: {self.department}, Salary: ${self._salary}, Team Size: {self.team_size}"

print("\n" + "=" * 50)
print("13. PRACTICAL EXAMPLE: COMPANY SYSTEM")
print("=" * 50)
emp1 = Employee("Alice", "IT", 50000)
emp2 = Employee("Bob", "HR", 45000)
manager = Manager("Charlie", "IT", 70000, 5)

print(emp1.display_info())
print(emp2.display_info())
print(manager.display_info())
print(f"Total Employees: {Employee.total_employees()}")


# ============================================
# 14. CLASS VARIABLES vs INSTANCE VARIABLES
# ============================================
print("\n" + "=" * 60)
print("14. CLASS VARIABLES vs INSTANCE VARIABLES")
print("=" * 60)
print("""
INSTANCE VARIABLES: Different for each object (self.var)
CLASS VARIABLES: Shared by all objects of the class
""")

class Student14:
    school = "ABC School"  # Class variable (shared)
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = Student14("Alice", 101)
s2 = Student14("Bob", 102)

print(f"Student 1: {s1.name} from {s1.school}")
print(f"Student 2: {s2.name} from {s2.school}")
print("Both have same school (Class Variable)")

s1.name = "Alicia"
print(f"Changed s1.name: {s1.name}, s2.name: {s2.name}")  # Different

Student14.school = "XYZ School"
print(f"Changed school: {s1.school}, {s2.school}")  # Same


# ============================================
# 15. STATIC METHODS (@staticmethod)
# ============================================
print("\n" + "=" * 60)
print("15. STATIC METHODS (@staticmethod)")
print("=" * 60)
print("""
Methods that don't need access to instance (self) or class (cls).
Called without creating object: ClassName.method()
""")

class MathOps:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b

print(f"10 + 5 = {MathOps.add(10, 5)}")
print(f"10 - 5 = {MathOps.subtract(10, 5)}")
print(f"10 * 5 = {MathOps.multiply(10, 5)}")


# ============================================
# 16. COMPOSITION (HAS-A RELATIONSHIP)
# ============================================
print("\n" + "=" * 60)
print("16. COMPOSITION (HAS-A RELATIONSHIP)")
print("=" * 60)
print("""
Using objects of one class inside another class.
Strong coupling - composed object cannot exist without parent.
Example: Car HAS Engine
""")

class Engine:
    def __init__(self, type_):
        self.type = type_
    
    def start(self):
        return f"{self.type} engine started!"

class Transmission:
    def __init__(self, type_):
        self.type = type_
    
    def shift(self):
        return f"Shifting {self.type} transmission"

class Car16:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = Engine("V8")
        self.transmission = Transmission("Automatic")

car16 = Car16("Toyota", "Camry")
print(f"{car16.brand} {car16.model}: {car16.engine.start()}")


# ============================================
# 17. ASSOCIATION (USES-A RELATIONSHIP)
# ============================================
print("\n" + "=" * 60)
print("17. ASSOCIATION (USES-A RELATIONSHIP)")
print("=" * 60)
print("""
Relationship between independent classes.
Looser coupling than composition.
Example: Author writes Book
""")

class Author:
    def __init__(self, name, country):
        self.name = name
        self.country = country

class Book17:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

author = Author("John Doe", "USA")
book = Book17("Python Guide", author, 300)

print(f"Book: {book.title}")
print(f"Author: {book.author.name} from {book.author.country}")


# ============================================
# 18. METHOD CHAINING
# ============================================
print("\n" + "=" * 60)
print("18. METHOD CHAINING")
print("=" * 60)
print("""
Calling multiple methods in a single statement.
Methods return 'self' to enable chaining.
""")

class Calculator:
    def __init__(self, value=0):
        self.value = value
    
    def add(self, num):
        self.value += num
        return self
    
    def subtract(self, num):
        self.value -= num
        return self
    
    def multiply(self, num):
        self.value *= num
        return self
    
    def get_result(self):
        return self.value

result = Calculator(10).add(5).subtract(3).multiply(2).get_result()
print(f"Result of chaining: {result}")  # ((10 + 5 - 3) * 2) = 24


# ============================================
# 19. SUPER() FUNCTION
# ============================================
print("\n" + "=" * 60)
print("19. SUPER() FUNCTION")
print("=" * 60)
print("""
Calls methods from the parent class in the child class.
Used to access parent class methods when overridden.
""")

class Vehicle19:
    def __init__(self, brand):
        self.brand = brand
    
    def display(self):
        return f"Brand: {self.brand}"

class Car19(Vehicle19):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def display(self):
        return f"{super().display()}, Model: {self.model}"

car19 = Car19("Honda", "Accord")
print(car19.display())


# ============================================
# 20. HIERARCHICAL INHERITANCE
# ============================================
print("\n" + "=" * 60)
print("20. HIERARCHICAL INHERITANCE")
print("=" * 60)
print("""
Multiple child classes inherit from one parent class.
""")

class Shape20:
    def __init__(self, color):
        self.color = color

class Rectangle20(Shape20):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle20(Shape20):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

rect = Rectangle20("Red", 5, 10)
circle = Circle20("Blue", 7)
print(f"Rectangle area: {rect.area()}")
print(f"Circle area: {circle.area()}")


# ============================================
# SUMMARY OF KEY OOP CONCEPTS
# ============================================
print("\n" + "=" * 60)
print("SUMMARY OF KEY OOP PRINCIPLES")
print("=" * 60)

summary = {
    "Encapsulation": "Hide internal details, expose only necessary",
    "Inheritance": "Reuse code through parent-child relationships",
    "Polymorphism": "Same interface, different implementations",
    "Abstraction": "Show essential features, hide complexity"
}

for concept, definition in summary.items():
    print(f"{concept}: {definition}")

print("\n" + "=" * 60)
print("OOP CONCEPTS COMPLETED!")
print("=" * 60)