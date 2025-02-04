# Object-Oriented Programming (OOP)

## 1. **Introduction to OOP**

### What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data and code to manipulate that data. It is designed to facilitate code reusability, scalability, and maintainability. OOP is widely used in modern programming languages such as Java, Python, C++, and C#.

### Key Concepts of OOP

#### Encapsulation
Encapsulation is the technique of bundling data (variables) and methods (functions) that operate on the data into a single unit, known as a class. This helps to protect the integrity of the data by restricting direct access from outside the class. Access modifiers such as `private`, `public`, and `protected` control visibility.

Example in Python:
```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model
    
    def get_brand(self):
        return self.__brand  # Encapsulated data access
```

#### Inheritance
Inheritance allows one class (child) to inherit attributes and behaviors (methods) from another class (parent). This promotes code reusability and a hierarchical relationship between classes.

Example in Python:
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):  # Inheriting from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
```

#### Polymorphism
Polymorphism allows methods to have the same name but behave differently depending on the object calling them. It enables flexibility and a more generic approach to programming.

Example in Python:
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"
```

#### Abstraction
Abstraction is the process of hiding complex implementation details and exposing only necessary functionality. This simplifies interaction with objects by reducing complexity.

Example in Python using `ABC` (Abstract Base Class):
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"
```

By applying these fundamental OOP principles, developers can create more organized, maintainable, and scalable software applications.
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)
```
