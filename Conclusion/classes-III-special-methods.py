# Classes III: Special Methods
# Written by Gower Campbell
# Enhanced and structured by AI

# -----------------------------------------------------------------------------
# Introduction to Special Methods
# -----------------------------------------------------------------------------

"""
Special methods in Python, also known as magic methods or dunder methods (double underscore),
are predefined methods that allow developers to define how objects of a class should behave
in certain situations. These methods begin and end with double underscores, like __init__,
__str__, and __repr__. They enable custom objects to integrate seamlessly with Python's
built-in features, such as string representations, arithmetic operations, comparisons, and more.

Special methods enhance object-oriented programming by allowing you to create well-structured
classes that behave like built-in types. They influence how objects interact with Python's
core functionalities, such as printing, iteration, and comparison.
"""

# -----------------------------------------------------------------------------
# Constructors and Destructors
# -----------------------------------------------------------------------------

# __init__ (Constructor)
"""
The __init__ method is the most common special method. It initializes instance variables
and runs setup code when an object is created. It is automatically called when you create
an instance of a class.
"""

class Student:
    def __init__(self, fullname, student_number):
        self.fullname = fullname
        self.student_number = student_number

new_student = Student("John McClane", "DH736648")

# __del__ (Destructor)
"""
The __del__ method is called when an object is about to be destroyed. It is used for cleanup
operations, such as closing files or releasing resources.
"""

class FileManager:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print(f"Opened {filename}")

    def __del__(self):
        self.file.close()
        print("File closed.")

file_manager = FileManager("example.txt")
file_manager.file.write("Hello, World!")
# When the object is destroyed, __del__ is called, closing the file.

# -----------------------------------------------------------------------------
# String Representation of Objects
# -----------------------------------------------------------------------------

# __repr__
"""
The __repr__ method returns an official string representation of an object, primarily used
for debugging and development. It should include detailed information about the object's state.
"""

class Student:
    def __init__(self, fullname, student_number):
        self.fullname = fullname
        self.student_number = student_number

    def __repr__(self):
        return (f"<Student(name={self.fullname!r}, "
                f"S_Number={self.student_number!r}, "
                f"id={hex(id(self))})>")

new_student = Student("Percy Jackson", "PJ323423")
print(new_student)
# Output: <Student(name='Percy Jackson', S_Number='PJ323423', id=0x7f8c1d2e3d90)>

# __str__
"""
The __str__ method returns a user-friendly string representation of an object. It is called
by the print() function and str().
"""

class Student:
    def __init__(self, full_name, student_number):
        self.full_name = full_name
        self.student_number = student_number
    
    def __str__(self):
        return (f"Full Name: \t{self.full_name}\n"
                f"Student Num: \t{self.student_number}")

new_student = Student("Percy Jackson", "PJ323423")
print(new_student)
# Output: Full Name: Percy Jackson
#         Student Num: PJ323423

# -----------------------------------------------------------------------------
# Container-Like Objects
# -----------------------------------------------------------------------------

"""
Container-like objects are objects that can hold or store other objects, such as lists or
dictionaries. By implementing special methods, you can make your custom objects behave like
containers.
"""

# Key Characteristics of Container-Like Objects:
"""
- Holds Multiple Items: Can store more than one value.
- Supports Iteration: Can be looped over.
- Dynamic Sizing: Can grow or shrink as items are added or removed.
- Indexing & Slicing: Supports accessing items using indices.
"""

# Example: Implementing Container-Like Behavior
class ContactList:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def __getitem__(self, key):
        return self.contact_list[key]
    
contact_list = ContactList()
contact_list.add_contact("Test Contact")
print(contact_list[0])  # Output: Test Contact

# Common Container Methods:
"""
- len(object) → __len__(self)
- object[key] → __getitem__(self, key)
- object[key] = item → __setitem__(self, key, item)
- item in object → __contains__(self, item)
"""

# -----------------------------------------------------------------------------
# Comparators
# -----------------------------------------------------------------------------

"""
Special methods allow you to define how objects are compared. For example, when comparing
two objects using >, the __gt__ method is called.
"""

# Example: Comparing Students by Average
class Student:
    def __init__(self, fullname, student_number, average):
        self.fullname = fullname
        self.student_number = student_number
        self.average = average

    def __gt__(self, other):
        return self.average > other.average

student1 = Student("Peter Parker", "PP123", 88)
student2 = Student("Tony Stark", "TS456", 97)
print(student1 > student2)  # Output: False

# Common Comparator Methods:
"""
- x == y → __eq__(self, other)
- x != y → __ne__(self, other)
- x < y → __lt__(self, other)
- x <= y → __le__(self, other)
- x > y → __gt__(self, other)
- x >= y → __ge__(self, other)
"""

# -----------------------------------------------------------------------------
# Polymorphism
# -----------------------------------------------------------------------------

"""
Polymorphism allows objects of different classes to respond to the same method call in
different ways. It is a key concept in object-oriented programming.
"""

# Method Overriding
"""
Method overriding occurs when a subclass provides a specific implementation of a method
that is already defined in its parent class.
"""

class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Lion(Animal):
    def make_sound(self):
        return "Roar"

def animal_sound(animal):
    print(animal.make_sound())

generic_animal = Animal()
lion = Lion()

animal_sound(generic_animal)  # Output: Some generic animal sound
animal_sound(lion)  # Output: Roar

# Operator Overloading
"""
Operator overloading allows you to define how operators like +, -, *, etc., behave for
your objects.
"""

class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

num1 = MyNumber(10)
num2 = MyNumber(5)
num3 = num1 + num2
print(num3.value)  # Output: 15

# Duck Typing
"""
Duck typing is a concept where the type or class of an object is less important than the
methods or properties it possesses. If an object behaves like a duck (i.e., has the required
methods), it can be treated as a duck.
"""

class Dog:
    def speak(self):
        print("WOOF!")

class Cat:
    def speak(self):
        print("MEOW!")

class Car:
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------

"""
- Special Methods: We explored __init__, __del__, __repr__, and __str__ for object
  initialization, destruction, and string representation.

- Constructors and Destructors: __init__ initializes objects, while __del__ cleans up
  before objects are destroyed.

- Container-Like Objects: We learned how to make objects behave like containers using
  __len__, __getitem__, etc.

- Comparators: We covered how to use special methods like __lt__ for comparing objects.

- Polymorphism: We discussed method overriding, operator overloading, and duck typing
  to make our code flexible and adaptable.
"""
