# **Inheritance**
   - [Base Class and Derived Class](#base-class-and-derived-class)
   - [Method Overriding](#method-overriding)
   - [Using `super()`](#using-super)
   - [Multiple Inheritance](#Multiple-Inheritance)
   - [Abstract Base Classes (ABCs)](#Abstract-Base-Classes-(ABCs))

Let’s dive more into **Inheritance**, one of the core concepts of Object-Oriented Programming (OOP). Inheritance allows a class (called a **derived class** or **child class**) to inherit attributes and methods from another class (called a **base class** or **parent class**). This promotes code reusability and a hierarchical structure.

---

## **Base Class and Derived Class**
- **Base Class (Parent Class)**: The class whose attributes and methods are inherited.
- **Derived Class (Child Class)**: The class that inherits from the base class.

#### Example:
```python
# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived Class
class Dog(Animal):  # Inherits from Animal
    def bark(self):
        return f"{self.name} says woof!"

# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Accessing methods
print(animal.speak())  # Output: Generic Animal makes a sound.
print(dog.speak())     # Output: Buddy makes a sound. (inherited from Animal)
print(dog.bark())      # Output: Buddy says woof! (defined in Dog)
```

---

## **Method Overriding**
When a derived class defines a method with the same name as a method in the base class, the derived class’s method **overrides** the base class’s method. This allows the derived class to provide a specific implementation of the method.

#### Example:
```python
# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived Class
class Cat(Animal):
    def speak(self):  # Overrides the speak() method in Animal
        return f"{self.name} says meow!"

# Creating objects
animal = Animal("Generic Animal")
cat = Cat("Whiskers")

# Accessing overridden method
print(animal.speak())  # Output: Generic Animal makes a sound.
print(cat.speak())     # Output: Whiskers says meow! (overridden method)
```

---

## **Using `super()`**
The `super()` function is used to call a method from the base class. This is particularly useful when you want to extend the functionality of the base class method rather than completely overriding it.

#### Example:
```python
# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the base class's __init__ method
        self.breed = breed

    def speak(self):
        # Extend the base class's speak() method
        return f"{super().speak()} {self.name} is a {self.breed} and says woof!"

# Creating an object
dog = Dog("Buddy", "Golden Retriever")

# Accessing methods
print(dog.speak())  # Output: Buddy makes a sound. Buddy is a Golden Retriever and says woof!
```

---

### **Key Takeaways**
1. **Inheritance**: A derived class inherits attributes and methods from a base class.
2. **Method Overriding**: A derived class can provide its own implementation of a method defined in the base class.
3. **`super()`**: Used to call a method from the base class, often to extend its functionality.

---

### **Advanced Example: Multi-Level Inheritance**
Inheritance can be chained, creating a hierarchy of classes.

```python
# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived Class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

# Derived Class 2
class Puppy(Dog):  # Inherits from Dog
    def play(self):
        return f"{self.name} is playing!"

# Creating an object
puppy = Puppy("Max")

# Accessing methods
print(puppy.speak())  # Output: Max says woof! (inherited from Dog)
print(puppy.play())   # Output: Max is playing! (defined in Puppy)
```

---

### **When to Use Inheritance?**
- When you want to create a new class that is a specialized version of an existing class.
- When you want to reuse code and avoid duplication.
- When you want to establish a logical hierarchy between classes.

---

## **Multiple Inheritance**
Multiple Inheritance allows a class to inherit attributes and methods from **more than one base class**. This can be useful for combining functionalities from different classes, but it requires careful design to avoid conflicts (e.g., the **diamond problem**).

### **Example of Multiple Inheritance**
```python
# Base Class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Base Class 2
class CanFly:
    def fly(self):
        return f"{self.name} is flying!"

# Base Class 3
class CanSwim:
    def swim(self):
        return f"{self.name} is swimming!"

# Derived Class (inherits from Animal, CanFly, and CanSwim)
class Duck(Animal, CanFly, CanSwim):
    def speak(self):  # Overrides the speak() method in Animal
        return f"{self.name} says quack!"

# Creating an object
duck = Duck("Donald")

# Accessing methods from all base classes
print(duck.speak())  # Output: Donald says quack! (from Duck)
print(duck.fly())    # Output: Donald is flying! (from CanFly)
print(duck.swim())   # Output: Donald is swimming! (from CanSwim)
```

---

### **The Diamond Problem**
Multiple Inheritance can lead to the **diamond problem**, where a class inherits from two classes that both inherit from the same base class. Python resolves this using the **Method Resolution Order (MRO)**, which determines the order in which base classes are searched for a method or attribute.

#### Example:
```python
class A:
    def greet(self):
        return "Hello from A!"

class B(A):
    def greet(self):
        return "Hello from B!"

class C(A):
    def greet(self):
        return "Hello from C!"

class D(B, C):
    pass

# Creating an object
d = D()

# Accessing the greet() method
print(d.greet())  # Output: Hello from B! (because of MRO: D -> B -> C -> A)
```

You can check the MRO using the `.__mro__` attribute:
```python
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

---

## **Abstract Base Classes (ABCs)**
An **Abstract Base Class** is a class that cannot be instantiated on its own and is meant to be subclassed. It defines a blueprint for other classes, ensuring that derived classes implement specific methods.

Python provides the `abc` module to create Abstract Base Classes.

### **Example of Abstract Base Class**
```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Derived classes must implement this method

    @abstractmethod
    def perimeter(self):
        pass  # Derived classes must implement this method

# Derived Class 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Derived Class 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Accessing methods
print(circle.area())       # Output: 78.5
print(rectangle.perimeter())  # Output: 20

# Trying to instantiate the abstract class (will raise an error)
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
```

---

### **Key Takeaways**
1. **Multiple Inheritance**: A class can inherit from multiple base classes. Use it carefully to avoid conflicts.
2. **Method Resolution Order (MRO)**: Determines the order in which base classes are searched for methods or attributes.
3. **Abstract Base Classes (ABCs)**: Define a blueprint for other classes. They cannot be instantiated and require derived classes to implement specific methods.

---

### **When to Use Multiple Inheritance?**
- When you need to combine functionalities from multiple classes.
- When you want to create a class that is a combination of several independent classes.

---

### **When to Use Abstract Base Classes?**
- When you want to enforce a common interface or structure for derived classes.
- When you want to ensure that certain methods are implemented in all subclasses.

---

### **Full Example: Combining Multiple Inheritance and ABCs**
```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

# Base Class 1
class Engine:
    def start(self):
        return "Engine started."

# Base Class 2
class Fuel:
    def fill_fuel(self, amount):
        return f"Fuel tank filled with {amount} liters."

# Derived Class (inherits from Vehicle, Engine, and Fuel)
class Car(Vehicle, Engine, Fuel):
    def move(self):
        return "Car is moving on the road."

# Creating an object
car = Car()

# Accessing methods
print(car.start())       # Output: Engine started. (from Engine)
print(car.fill_fuel(50)) # Output: Fuel tank filled with 50 liters. (from Fuel)
print(car.move())        # Output: Car is moving on the road. (from Vehicle)
```

