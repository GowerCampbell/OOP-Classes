# Classes II
# Written by Gower Campbell
# Enhanced and structured by AI

# -----------------------------------------------------------------------------
# The Role of the __init__ Method
# -----------------------------------------------------------------------------

"""
The __init__ method is used to define the class-level methods that can modify
the class-level attributes. It is automatically called when an object is created.
"""

# -----------------------------------------------------------------------------
# The @staticmethod Decorator
# -----------------------------------------------------------------------------

"""
The @staticmethod decorator allows the definition of a method that does not
require access to the instance (self) or class (cls) parameters. It can be
called on the class itself or on its instances, and it does not modify
class or instance state. It is used for utility functions that perform
a task in isolation from the class or instance context.
"""

# -----------------------------------------------------------------------------
# Inheritance in OOP
# -----------------------------------------------------------------------------

"""
Inheritance is a fundamental concept in OOP where a new class (subclass) is
derived from an existing class (base class). It allows for code reuse and
extensibility by inheriting attributes and methods from the parent class.
"""

# Key Components of Inheritance:
"""
- Base Class (Parent Class): The class being inherited from.
- Derived Class (Subclass): The class that inherits from the base class.
"""

# Benefits of Inheritance:
"""
- Code Reuse: Reuse attributes and methods from the parent class.
- Organized Structure: Creates a hierarchy of classes.
- Extensibility: Enables easy extension and modification of existing classes.
"""

# Example: Animal Kingdom
"""
- Base Class: Animal (parent to all animals).
- Subclasses: Mammal, Reptile, Bird, Fish.
"""

# Syntax:
"""
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass
"""

# Inheritance Hierarchy:
"""
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

class GrandChildClass(ChildClass):
    pass
"""

# Example:
class Animal:
    def __init__(self, name, species, number_of_legs):
        self.name = name
        self.species = species
        self.number_of_legs = number_of_legs

    def speak(self):
        print("This animal speaks")
    
    def eat(self):
        print("This animal eats")

    def display_info(self):
        print(f"This is a {self.species} named {self.name} and has {self.number_of_legs} legs")

class Dog(Animal):
    pass

my_dog = Dog("Rex", "Dog", 4)
print(my_dog.name)  # Output: Rex
print(my_dog.species)  # Output: Dog
print(my_dog.number_of_legs)  # Output: 4
my_dog.display_info()  # Output: This is a Dog named Rex and has 4 legs

# -----------------------------------------------------------------------------
# Method Overriding
# -----------------------------------------------------------------------------

"""
Method overriding is the process of re-implementing a method already defined
in a superclass to provide a specific implementation in the subclass.
"""

# Syntax:
"""
class ParentClass:
    def method_name(self):
        pass

class ChildClass(ParentClass):
    def method_name(self):
        pass
"""

# Example:
class Animal:
    def speak(self):
        return "makes a sound"
    
    def eat(self):
        return "eats food"

class Dog(Animal):
    def speak(self):
        return "barks"
    
    def eat(self):
        return "eats bones"

generic_animal = Animal()
print(generic_animal.speak())  # Output: makes a sound
print(generic_animal.eat())  # Output: eats food

my_dog = Dog()
print(my_dog.speak())  # Output: barks
print(my_dog.eat())  # Output: eats bones

# -----------------------------------------------------------------------------
# Using super()
# -----------------------------------------------------------------------------

"""
The super() function is used to extend the functionality of the parent class
to the child class. It allows the child class to access the parent class's
methods and attributes, avoiding redundancy in the code.
"""

# Syntax:
"""
class ParentClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

class ChildClass(ParentClass):
    def __init__(self, attribute1, attribute2, attribute3):
        super().__init__(attribute1, attribute2)
        self.attribute3 = attribute3
"""

# Example:
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

my_dog = Dog("Rex", 5, "Labrador")
print(my_dog.name)  # Output: Rex
print(my_dog.age)  # Output: 5
print(my_dog.breed)  # Output: Labrador

# Example 2:
class Animal:
    def speak(self):
        return "This animal speaks"
    
class Dog(Animal):
    def speak(self):
        """Override the speak method in the parent class
        and extend the functionality of the parent class."""
        return super().speak() + " and barks"
    
my_dog = Dog()
print(my_dog.speak())  # Output: This animal speaks and barks

# -----------------------------------------------------------------------------
# Conclusion
# -----------------------------------------------------------------------------

"""
- Inheritance: Inherits attributes and methods from a superclass; allows for
  code reuse and extensibility of a structured class hierarchy.
- Superclass & Subclass: Parent class and child class relationship; extends
  the functionality of the parent class.
- Method Overriding: Re-implementing a method in the subclass to provide
  a specific implementation.
- super(): Accesses the parent class methods and attributes in the child class.
- Benefits: Simplifies code, promotes code reuse, and enables extensibility.
"""

# -----------------------------------------------------------------------------
# Vehicle Rental Service Implementation
# -----------------------------------------------------------------------------

"""
Objective: To create a Vehicle Rental Service using inheritance, where each
vehicle type (Car, Bike) can calculate its rental cost based on the number of
days rented. The system should handle exceptions such as negative days and
invalid input types.
"""

# Base Class: Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_details(self):
        """Return the details of the vehicle."""
        return f"{self.year} {self.make} {self.model}"

    def rent(self):
        """Generic rent method for vehicles."""
        return "Renting this vehicle."

    def calculate_rental_cost(self, days):
        """Calculate rental cost based on number of days."""
        if not isinstance(days, int) or days < 0:
            raise ValueError("Number of days must be a non-negative integer.")
        return days * 50  # Generic cost, can be overridden by subclasses

# Subclass: Car
class Car(Vehicle):
    def rent(self):
        """Specific rent method for cars."""
        return "Renting a car."

    def calculate_rental_cost(self, days):
        """Calculate rental cost for cars."""
        if not isinstance(days, int) or days < 0:
            raise ValueError("Number of days must be a non-negative integer.")
        return days * 70  # Cars have a higher daily rental cost

# Subclass: Bike
class Bike(Vehicle):
    def rent(self):
        """Specific rent method for bikes."""
        return "Renting a bike."

    def calculate_rental_cost(self, days):
        """Calculate rental cost for bikes."""
        if not isinstance(days, int) or days < 0:
            raise ValueError("Number of days must be a non-negative integer.")
        return days * 30  # Bikes have a lower daily rental cost

# Example Usage
try:
    my_car = Car("Toyota", "Corolla", 2020)
    print(my_car.get_details())  # Output: 2020 Toyota Corolla
    print(my_car.rent())         # Output: Renting a car.
    print(f"Rental Cost: £{my_car.calculate_rental_cost(5)}")  # Output: £350

    my_bike = Bike("Yamaha", "YZF-R3", 2022)
    print(my_bike.get_details())  # Output: 2022 Yamaha YZF-R3
    print(my_bike.rent())         # Output: Renting a bike.
    print(f"Rental Cost: £{my_bike.calculate_rental_cost(3)}")  # Output: £90

    # Handling invalid input
    print(my_car.calculate_rental_cost(-2))  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

# End of File
