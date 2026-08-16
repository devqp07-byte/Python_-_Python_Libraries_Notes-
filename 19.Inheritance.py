"""                         ============================================================
                                                 #NOTE:--> INHERITANCE 
                            ============================================================
"""

# ------------------------------------------------------------
## 1. WHAT IS INHERITANCE ?
# ------------------------------------------------------------
# Inheritance means:
# One class can use properties (variables) and methods (functions)
# of another class.

# Parent Class / Base Class / Superclass  → The class being inherited
# Child Class / Derived Class / Subclass  → The class that inherits

# Real Life Example:
# Father → Child
# Child gets features from Father


# ------------------------------------------------------------
## 2. BASIC SYNTAX
# ------------------------------------------------------------

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):     # Child inherits Parent
    def display(self):
        print("This is Child class")

obj = Child()
obj.show()      # inherited method
obj.display()


# ------------------------------------------------------------
## 3. WHY WE USE INHERITANCE ?
# ------------------------------------------------------------
# ✅ Code Reusability
# ✅ Less duplication
# ✅ Easy maintenance
# ✅ Real world relationship modeling


# ------------------------------------------------------------
## 4. TYPES OF INHERITANCE IN PYTHON
# ------------------------------------------------------------

# 1️⃣ Single Inheritance
# 2️⃣ Multiple Inheritance
# 3️⃣ Multilevel Inheritance
# 4️⃣ Hierarchical Inheritance
# 5️⃣ Hybrid Inheritance


# ------------------------------------------------------------
## 5. SINGLE INHERITANCE
## One Parent → One Child
# ------------------------------------------------------------

class Father:
    def money(self):
        print("Father has money")

class Son(Father):
    def bike(self):
        print("Son has bike")

obj = Son()
obj.money()
obj.bike()


# ------------------------------------------------------------
## 6. MULTILEVEL INHERITANCE
## Grandparent → Parent → Child
# ------------------------------------------------------------

class Grandfather:
    def land(self):
        print("Grandfather land")

class Father(Grandfather):
    def house(self):
        print("Father house")

class Son(Father):
    def car(self):
        print("Son car")

obj = Son()
obj.land()
obj.house()
obj.car()


# ------------------------------------------------------------
## 7. MULTIPLE INHERITANCE
## Child inherits from multiple parents
# ------------------------------------------------------------

class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Coding")

obj = Child()
obj.skill1()
obj.skill2()
obj.skill3()


# ------------------------------------------------------------
## 8. HIERARCHICAL INHERITANCE
## One Parent → Multiple Children
# ------------------------------------------------------------

class Parent:
    def home(self):
        print("Parent Home")

class Son(Parent):
    pass

class Daughter(Parent):
    pass

s = Son()
d = Daughter()

s.home()
d.home()


# ------------------------------------------------------------
## 9. HYBRID INHERITANCE
## Combination of multiple inheritance types
# ------------------------------------------------------------

class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):
    def showD(self):
        print("Class D")

obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()


# ------------------------------------------------------------
## 10. CONSTRUCTOR IN INHERITANCE (__init__)
# ------------------------------------------------------------

class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()      # call parent constructor
        print("Child Constructor")

obj = Child()


# ------------------------------------------------------------
## 11. super() FUNCTION (VERY IMPORTANT)
# ------------------------------------------------------------
# super() is used to call parent class methods or constructor.

class Parent:
    def show(self):
        print("Parent Method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child Method")

obj = Child()
obj.show()


# ------------------------------------------------------------
## 12. METHOD OVERRIDING
# ------------------------------------------------------------
# Child class changes parent method implementation.

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

obj = Child()
obj.show()     # Child method runs


# ------------------------------------------------------------
## 13. METHOD RESOLUTION ORDER (MRO)
# ------------------------------------------------------------
# Python decides which method to run using MRO.

class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())   # shows order


# ------------------------------------------------------------
## 14. IMPORTANT INTERVIEW QUESTIONS
# ------------------------------------------------------------

# Q1: Can child access parent private variable?
# Yes, using name mangling (_ClassName__var)

class Parent:
    def __init__(self):
        self.__money = 1000

class Child(Parent):
    def show(self):
        print(self._Parent__money)

obj = Child()
obj.show()


# ------------------------------------------------------------
## 15. KEY POINTS TO MASTER
# ------------------------------------------------------------

# ✔ Inheritance promotes code reuse
# ✔ Use super() to call parent constructor
# ✔ Method overriding changes behavior
# ✔ Python supports multiple inheritance
# ✔ MRO decides method calling order


# ------------------------------------------------------------
## 16. PRO LEVEL UNDERSTANDING
# ------------------------------------------------------------

# isinstance() → checks object type
# issubclass() → checks class relationship

class A:
    pass

class B(A):
    pass

obj = B()

print(isinstance(obj, B))   # True
print(isinstance(obj, A))   # True
print(issubclass(B, A))     # True


""" 
========================================
          #! End of Inheritense
========================================
"""


#? Example:--

#! main class:----->

class parent:
    def __init__(self, name, age, city):
        self.name = name 
        self.age = age
        self.city = city

    def info(self):
        return f"My name is {self.name}. I am {self.age} years old. I am living in {self.city}."

#! child calss:----->

class child(parent):
    def __init__(self, name, age, city, gender, skill):
        super().__init__(name, age, city)
        self.gender = gender
        self.skill = skill 

    def info(self):
        return f"My name is {self.name}. I am {self.age} years old. I am living in {self.city}. My gender is {self.gender}. My skill is {self.skill}."
    
# Note:- create object using "child" class:----->
user = child("Ayushi Jain", 45, "New Delhi", "Female", "React-Native")
print(user.info())