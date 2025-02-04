### **Classes and Objects**
   - [Defining a Class](#Defining-a-Class)
   - [Creating Objects](#Creating-Object)
   - [Instance Attributes vs Class Attributes](#Instance-Attributes-vs-Class-Attributes)
   - [The `__init__` Method](#The-`__init__`-Method)
   - [The Role of `self`](#The-Role-of-`self)

## **Defining a Class**
A class is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Instance attributes (unique to each instance)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method (behavior)
    def bark(self):
        return f"{self.name} says woof!"
```

## **Creating Objects**
An object is an instance of a class. You create an object by calling the class as if it were a function.

```python
# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Milo", 3)

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
print(dog2.bark())  # Output: Milo says woof!
```

## **Instance Attributes vs Class Attributes**
- **Instance Attributes:** Unique to each object. Defined inside the `__init__` method using `self`.
- **Class Attributes:** Shared by all instances of the class. Defined directly inside the class.

```python
print(dog1.species)  # Output: Canis familiaris (class attribute)
print(dog2.species)  # Output: Canis familiaris (class attribute)

dog1.species = "Canis lupus"  # Modifying class attribute for dog1 only
print(dog1.species)  # Output: Canis lupus
print(dog2.species)  # Output: Canis familiaris (unchanged)
```

## **The `__init__` Method**
The `__init__` method is a special method in Python classes. It is called automatically when a new object is created. It is used to initialize the object's attributes.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
```

## **The Role of `self`**
`self` refers to the instance of the class. It is used to access instance attributes and methods.

When you call a method on an object, Python automatically passes the object as the first argument (`self`).

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# When you call dog1.bark(), Python translates it to Dog.bark(dog1)
print(dog1.bark())  # Output: Buddy says woof!
```

## **Summary**
- A **class** is a blueprint for creating objects.
- An **object** is an instance of a class.
- **Instance attributes** are unique to each object, while **class attributes** are shared by all instances.
- The `__init__` method initializes object attributes.
- `self` refers to the instance and is used to access its attributes and methods. or examples! 🚀
