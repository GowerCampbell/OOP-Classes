
## Introduction to OOP

### What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods). OOP organizes software design around data, rather than functions and logic.

### Key Concepts of OOP
- **Encapsulation**: Bundling data and methods that operate on that data.
- **Inheritance**: Creating new classes based on existing classes.
- **Polymorphism**: Objects of different classes can be treated as objects of a common base class.
- **Abstraction**: Simplifying complex systems by modeling classes based on real-world entities.

---

## Classes and Objects

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

## Inheritance

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
