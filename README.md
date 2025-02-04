# Object-Oriented Programming (OOP) Guide

This guide provides a comprehensive overview of Object-Oriented Programming (OOP) concepts, including classes, objects, inheritance, encapsulation, polymorphism, and more. It also includes practical examples and code snippets to help you understand and implement OOP principles in Python.

---

## Table of Contents

1. **Introduction to OOP**
   - [What is OOP?](#what-is-oop)
   - [Key Concepts of OOP](#key-concepts-of-oop)
     - Encapsulation
     - Inheritance
     - Polymorphism
     - Abstraction

2. **Classes and Objects**
   - [Defining a Class](#defining-a-class)
   - [Creating Objects](#creating-objects)
   - [Instance Attributes vs Class Attributes](#instance-attributes-vs-class-attributes)
   - [The `__init__` Method](#the-__init__-method)
   - [The Role of `self`](#the-role-of-self)

3. **Encapsulation**
   - [Private Attributes](#private-attributes)
   - [Getter and Setter Methods](#getter-and-setter-methods)

4. **Inheritance**
   - [Base Class and Derived Class](#base-class-and-derived-class)
   - [Method Overriding](#method-overriding)
   - [Using `super()`](#using-super)

5. **Polymorphism**
   - [Method Overriding](#method-overriding)
   - [Operator Overloading](#operator-overloading)
   - [Duck Typing](#duck-typing)

6. **Special Methods (Magic/Dunder Methods)**
   - [Constructors and Destructors](#constructors-and-destructors)
     - `__init__`
     - `__del__`
   - [String Representation](#string-representation)
     - `__repr__`
     - `__str__`
   - [Container-Like Objects](#container-like-objects)
     - `__len__`
     - `__getitem__`
   - [Comparators](#comparators)
     - `__eq__`, `__lt__`, `__gt__`, etc.

7. **Static and Class Methods**
   - [Static Methods](#static-methods)
   - [Class Methods](#class-methods)

8. **Practical Examples**
   - [Car Management System](#car-management-system)
   - [Vehicle Rental Service](#vehicle-rental-service)
   - [Library Management System](#library-management-system)
   - [Employee Onboarding System](#employee-onboarding-system)
   - [Smart Device Management](#smart-device-management)

9. **Advanced Topics**
   - [Lambda Functions and Functional Programming](#lambda-functions-and-functional-programming)
   - [Decorators](#decorators)

10. **Conclusion**
    - [Summary of OOP Concepts](#summary-of-oop-concepts)
    - [Benefits of OOP](#benefits-of-oop)

---

## 1. Introduction to OOP

### What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods). OOP organizes software design around data, rather than functions and logic.

### Key Concepts of OOP
- **Encapsulation**: Bundling data and methods that operate on that data.
- **Inheritance**: Creating new classes based on existing classes.
- **Polymorphism**: Objects of different classes can be treated as objects of a common base class.
- **Abstraction**: Simplifying complex systems by modeling classes based on real-world entities.

---

## 2. Classes and Objects

### Defining a Class
A class is a blueprint for creating objects. It defines attributes (data) and methods (behaviors).

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"This is a {self.make} {self.model}")
```

### Creating Objects
Objects are instances of a class.

```python
my_car = Car("Toyota", "Corolla")
my_car.display_info()  # Output: This is a Toyota Corolla
```

### Instance Attributes vs Class Attributes
- **Instance Attributes**: Unique to each object.
- **Class Attributes**: Shared by all instances of the class.

```python
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age
```

### The `__init__` Method
The `__init__` method is a constructor that initializes object attributes.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### The Role of `self`
`self` refers to the current instance of the class and allows access to its attributes and methods.

---

## 3. Encapsulation

### Private Attributes
Private attributes are prefixed with an underscore (`_`) and are accessed via getter and setter methods.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self._model = model  # Private attribute

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model
```

### Getter and Setter Methods
These methods provide controlled access to private attributes.

```python
my_car = Car("Toyota", "Corolla")
print(my_car.get_model())  # Output: Corolla
my_car.set_model("Camry")
print(my_car.get_model())  # Output: Camry
```

---

## 4. Inheritance

### Base Class and Derived Class
Inheritance allows a class to inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

### Method Overriding
A subclass can override a method defined in its parent class.

```python
dog = Dog()
print(dog.speak())  # Output: Woof!
```

### Using `super()`
`super()` is used to call methods from the parent class.

```python
class Dog(Animal):
    def speak(self):
        return super().speak() + " and barks"
```

---

## 5. Polymorphism

### Method Overriding
Objects of different classes can respond to the same method call in different ways.

```python
class Lion(Animal):
    def speak(self):
        return "Roar"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())  # Output: Woof!
animal_sound(Lion())  # Output: Roar
```

### Operator Overloading
Define how operators like `+`, `-`, etc., behave for your objects.

```python
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)
```

### Duck Typing
If an object behaves like a duck, it can be treated as a duck.

```python
class Dog:
    def speak(self):
        print("WOOF!")

class Car:
    def speak(self):
        print("HONK!")

animals = [Dog(), Car()]
for animal in animals:
    animal.speak()
```

---

## 6. Special Methods (Magic/Dunder Methods)

### Constructors and Destructors
- `__init__`: Initializes object attributes.
- `__del__`: Called when an object is destroyed.

```python
class FileManager:
    def __init__(self, filename):
        self.file = open(filename, 'w')

    def __del__(self):
        self.file.close()
```

### String Representation
- `__repr__`: Official string representation for debugging.
- `__str__`: User-friendly string representation.

```python
class Student:
    def __repr__(self):
        return f"<Student(name={self.name}, age={self.age})>"

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"
```

### Container-Like Objects
Make objects behave like containers using `__len__`, `__getitem__`, etc.

```python
class ContactList:
    def __init__(self):
        self.contacts = []

    def __getitem__(self, key):
        return self.contacts[key]
```

### Comparators
Define how objects are compared using `__eq__`, `__lt__`, etc.

```python
class Student:
    def __gt__(self, other):
        return self.age > other.age
```

---

## 7. Static and Class Methods

### Static Methods
Static methods do not depend on class or instance data.

```python
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
```

### Class Methods
Class methods operate on the class itself.

```python
class MyClass:
    @classmethod
    def class_method(cls):
        return cls.class_attribute
```

---

## 8. Practical Examples

### Car Management System
A system to manage car information, including make, model, and rental cost.

### Vehicle Rental Service
A system to calculate rental costs for different vehicle types.

### Library Management System
A system to manage books, including adding, removing, and checking availability.

### Employee Onboarding System
A system to manage employee details, including name, age, department, and hobbies.

### Smart Device Management
A system to manage smart devices, including power status and energy consumption.

---

## 9. Advanced Topics

### Lambda Functions and Functional Programming
Lambda functions are small anonymous functions.

```python
calc = lambda num: "Even" if num % 2 == 0 else "Odd"
```

### Decorators
Decorators modify the behavior of functions.

```python
@staticmethod
def my_static_method():
    pass
```

---

## 10. Conclusion

### Summary of OOP Concepts
- Classes and Objects
- Encapsulation, Inheritance, Polymorphism, Abstraction
- Special Methods, Static and Class Methods

### Benefits of OOP
- Code Reusability
- Modularity
- Real-world Modeling
