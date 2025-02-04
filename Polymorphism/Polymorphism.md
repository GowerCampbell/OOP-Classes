# **Polymorphism in Object-Oriented Programming (OOP)**
   - [Method Overriding](#method-overriding)
   - [Operator Overloading](#operator-overloading)
   - [Duck Typing](#duck-typing)
     
---

## **Method Overriding**

Method overriding occurs when a subclass provides a specific implementation of a method already defined in its superclass. This allows the subclass to customize or extend the behavior of the method while maintaining a common interface.

### **Example:**
```python
# Base Class
class Animal:
    def speak(self):
        return "Animal makes a sound."

# Derived Class 1
class Dog(Animal):
    def speak(self):  # Overrides the speak() method in Animal
        return "Dog says woof!"

# Derived Class 2
class Cat(Animal):
    def speak(self):  # Overrides the speak() method in Animal
        return "Cat says meow!"

# Creating objects
animals = [Animal(), Dog(), Cat()]

# Demonstrating polymorphism
for animal in animals:
    print(animal.speak())
```
### **Output:**
```
Animal makes a sound.
Dog says woof!
Cat says meow!
```

### **Real-World Application:**
Consider a **payment processing system** where different payment methods (credit card, PayPal, bank transfer) override a common `process_payment()` method:
```python
class Payment:
    def process_payment(self, amount):
        return f"Processing payment of ${amount}."

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}."

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}."

# Using polymorphism
payments = [CreditCardPayment(), PayPalPayment()]
for payment in payments:
    print(payment.process_payment(100))
```
### **Output:**
```
Processing credit card payment of $100.
Processing PayPal payment of $100.
```

---

## **Operator Overloading**

Operator overloading allows you to define how operators (like `+`, `-`, `*`, etc.) behave for objects of a class. This is done by defining special methods (e.g., `__add__`, `__sub__`, `__mul__`) in the class.

### **Example:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overloading the * operator
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    # Overloading the string representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Creating objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Using overloaded operators
p3 = p1 + p2  # Calls __add__
p4 = p1 * 3   # Calls __mul__

print(p3)  # Output: Point(4, 6)
print(p4)  # Output: Point(3, 6)
```

### **Real-World Application:**
Consider a **shopping cart** where we overload the `+` operator to add products together:
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return Product(self.name + " & " + other.name, self.price + other.price)

    def __str__(self):
        return f"{self.name}: ${self.price}"

# Creating products
product1 = Product("Shoes", 50)
product2 = Product("Socks", 10)

# Adding products
bundle = product1 + product2
print(bundle)  # Output: Shoes & Socks: $60
```

---

## **Duck Typing**

Duck typing is a concept in Python where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type. The name comes from the phrase: *"If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."*

### **Example:**
```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

# Function that expects a "duck-like" object
def make_it_quack(duck_like_object):
    print(duck_like_object.quack())

# Creating objects
duck = Duck()
person = Person()

# Demonstrating duck typing
make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm quacking like a duck!
```

### **Real-World Application:**
Consider a **logging system** that works with any object as long as it has a `log()` method:
```python
class FileLogger:
    def log(self, message):
        print(f"Logging to a file: {message}")

class ConsoleLogger:
    def log(self, message):
        print(f"Logging to console: {message}")

# Function using duck typing
def log_message(logger, message):
    logger.log(message)

# Creating objects
file_logger = FileLogger()
console_logger = ConsoleLogger()

# Logging messages
log_message(file_logger, "File log entry")  # Logging to a file: File log entry
log_message(console_logger, "Console log entry")  # Logging to console: Console log entry
```

---

## **Key Takeaways**
1. **Method Overriding**: A subclass provides a specific implementation of a method defined in its superclass.
2. **Operator Overloading**: Define how operators behave for objects of a class using special methods like `__add__`, `__sub__`, etc.
3. **Duck Typing**: Focus on an object’s behavior (methods and properties) rather than its explicit type.

---

## **When to Use Polymorphism?**
- When you want to write flexible and reusable code that can work with objects of different classes.
- When you want to define a common interface for multiple classes.
- When you want to leverage operator overloading to make your classes more intuitive.


