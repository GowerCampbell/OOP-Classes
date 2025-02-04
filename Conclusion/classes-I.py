# Classes I
# Written by Gower Campbell

# -----------------------------------------------------------------------------
# Difference Between Procedural & Object-Oriented Programming (OOP)
# -----------------------------------------------------------------------------

"""
A programming paradigm based on the concept of "objects".
Objects contain attributes (data) and methods (behaviours).
OOP organizes software design around data, or objects, rather than functions and logic.
"""

# Key Concepts of OOP:
"""
1. Encapsulation: Bundling data & methods that operate on that data.
   - Hiding internal details while providing a public interface.
2. Inheritance: Creating new classes based on existing classes.
   - Promotes code reuse and hierarchy.
3. Polymorphism: Objects of different classes can be treated as objects of a common base class.
4. Abstraction: Simplifying complex systems by modelling classes and focusing on essentials.
"""

# -----------------------------------------------------------------------------
# Define a Class with Attributes & Methods
# -----------------------------------------------------------------------------

"""
A class is a blueprint for creating objects.
It defines attributes (data) and methods (behaviours).
- Attributes are the properties or characteristics of an object.
- Methods are the functions or operations that an object can perform.
"""

class Car:
    def __init__(self, make, model):
        self.make = make  # Instance Attributes
        self.model = model

    def display_info(self):  # Behaviour
        print(f"This is a {self.make} {self.model}")

# Creating an object
my_car = Car("Toyota", "Corolla")
print(my_car.make)  # Accessing attributes
my_car.model = "Camry"  # Modifying Attribute
my_car.display_info()  # Calling Method

# -----------------------------------------------------------------------------
# Interacting with Objects: The Dot Operator
# -----------------------------------------------------------------------------

"""
- Accessing attributes: object.attribute
- Calling methods: object.method()
- Modifying attributes: object.attribute = new_value
"""

# -----------------------------------------------------------------------------
# Implement Encapsulation Using Private Attributes
# -----------------------------------------------------------------------------

"""
Encapsulation is achieved by using private attributes (prefixed with an underscore).
Private attributes are accessed and modified using getter and setter methods.
"""

class Car:
    def __init__(self, make, model):
        self.make = make  # Public Attributes
        self._model = model  # Private attribute (underscore prefix)

    def get_model(self):
        return self._model  # Getter method for _model

    def set_model(self, model):
        self._model = model  # Setter method for _model

    def display_info(self):
        print(f"This is a {self.make} {self._model}")

# Creating an object
my_car = Car("Toyota", "Corolla")
my_car.display_info()  # Output: This is a Toyota Corolla

print(my_car.get_model())  # Output: Corolla
# Accessing a private attribute using a getter method

my_car.set_model("Camry")  # Modifying private attribute
my_car.display_info()  # Output: This is a Toyota Camry

# -----------------------------------------------------------------------------
# Explain the Role of Self in Methods
# -----------------------------------------------------------------------------

"""
- Self is a reference to the instance of the class.
- It is the first parameter in method definitions.
- Allows access to instance attributes and methods.
- Distinguishes instance variables from local variables.
"""

class Car:
    """Self allows us to access constructor attributes/data"""
    def __init__(self, make, model): 
        self.make = make
        self.model = model

    def display_info(self):
        print(f"This is a {self.make} {self.model}")  # Displays object's data

# Creating an object
my_car = Car("Toyota", "Corolla")
print(my_car.make)  # Output: Toyota
my_car.model = "Camry"  # Modifying attribute
my_car.display_info()  # Output: This is a Toyota Camry

# -----------------------------------------------------------------------------
# The Concept of Objects in OOP
# -----------------------------------------------------------------------------

"""
Objects are instances of classes.
- Combination of data (attributes) and methods (behaviours).
- Representation of real-world entities in code.
- Organizes and structures code.
- Creates reusable and modular code.
- Models real-world systems and relationships (Composition, Association, Aggregation, Inheritance).
"""

# Key Aspects of Objects:
"""
1. State: Data stored in the object (attributes).
2. Behaviour: What the object can do (methods).
3. Identity: Each object is unique.
4. Lifecycle: Creation, manipulation, and destruction.
"""

# Real-world example: Car
"""
- Attributes: Make, model, colour, year.
- Methods: Start, stop, drive, park.
- Identity: Licence plate number.
- Lifecycle: Manufacture, sale, maintenance, disposal.
"""

# -----------------------------------------------------------------------------
# Procedural vs OOP
# -----------------------------------------------------------------------------

# Procedural Programming
"""
Characteristics:
- Sequential, linear execution of code.
- Functions operating on data structures.
"""

# Example:
def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

# Usage:
length = 5
width = 3
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

# Object-Oriented Programming
"""
Characteristics:
- Objects as a combination of data and behaviours.
- Classes as blueprints for creating objects.
"""

# Advantages of OOP:
"""
- Encapsulation: Data protection and flexibility.
- Modularity: Code organization and reuse.
- Abstraction: Simplified complex systems.
- Reusability: Inheritance and polymorphism.
- Real-world modelling: Objects and relationships.
"""

# Example:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Usage:
rect = Rectangle(5, 3)
area = rect.calculate_area()
perimeter = rect.calculate_perimeter()

# -----------------------------------------------------------------------------
# Lesson Conclusion & Summary
# -----------------------------------------------------------------------------

"""
- Procedural vs. OOP: Different programming paradigms.
  - Procedural: Functions and data structures.
  - OOP: Objects and classes.
- Understanding Objects: Objects are instances of classes with combinations of data and methods.
- Classes & Attributes: Classes are blueprints for creating objects.
  - Attributes: Data stored in objects.
  - Methods: Functions that define object behaviour.
- __init__ Method & Dot Operator:
  - __init__ is a method for object initialization.
  - Dot operator: Accessing attributes and calling methods.
- Encapsulation and Self:
  - Encapsulation: Private attributes accessed via methods.
  - Public Methods: Access and modify private attributes.
  - Self: Reference to the instance of the class.
"""

# Example:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def update_year(self, new_year):
        self.year = new_year
    
    def display_info(self):
        return (f"This is a {self.year} {self.make} {self.model}")

# Creating an object    
my_car = Car("Toyota", "Corolla", 2015)

# Accessing attributes
print(my_car.display_info())
# Output: This is a 2015 Toyota Corolla

my_car.update_year(2018)
print(my_car.display_info())
# Output: This is a 2018 Toyota Corolla

# -----------------------------------------------------------------------------
# Lambda Functions and Functional Programming
# -----------------------------------------------------------------------------

# Lambda Function Example
"""
Lambda functions are small anonymous functions defined with the `lambda` keyword.
Syntax: lambda arguments: expression
"""

def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5]

# Lambda function to check if a number is even or odd
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))  # Output: Even number

# Using `reduce` from functools
"""
The `reduce` function applies a function cumulatively to the items of a sequence.
"""

from functools import reduce

def add(x, y):
    return x + y

res = reduce(add, a)  # Sum all elements in the list
print(res)  # Output: 15

# -----------------------------------------------------------------------------
# Decorators (for Later)
# -----------------------------------------------------------------------------

"""
Decorators are functions that modify the behavior of other functions.
Common decorators include @staticmethod and @classmethod.
"""

# Example (for future use):
@staticmethod
def my_static_method():
    pass

@classmethod
def my_class_method(cls):
    pass

# End of File
