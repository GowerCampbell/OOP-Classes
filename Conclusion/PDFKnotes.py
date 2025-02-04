'''OOP Classes''' # Written by Gower Campbell.

# Object oriented programming (OOP) is a fundamental style of 
# programming for developing larger pieces of software. 

# Object oriented programming, for example databases that record age, name 
# gender and this information we can use to represent this information in code.

# From defining a code (we can reuse) for grading.

# Think of the real-world implementations of the above systems will use OOP

# OOP Components
# Classes (Objects)
# In python, everything is an instance (object) of a class, i.e.
# strings, lists, dictionaries, etc. Everything has a blueprint that is
# based on a class.

# Each variable below is an instance of a class.
example_list = ["Dave", "Rob", "stephen"] # Instance of the 'list' class
example_boolean = True # instance of the bool class
example_string = "hello world" # instance of the 'str' class

# printing the type of each variable to verify their class
print(type(example_list)) # Output <class list>
print(type(example_boolean)) # Output <class bool>
print(type(example_string)) # Output <class str>

# Even a function is an instances of the 'function' class
def this_is_afunction(a, b):
    return a * b

# Verify the type of the function

print(type(this_is_afunction))

# split & strip are written into class and the str. 
# Adding email to a specfic class

"Everything in python is an object built from a particular class"

"Attributes" # Are varaiables that belong to an object defined in the class
# constructor using the _init_ method

"Method" #Function specfic to a class that operate on instances of that class.

'''CLASSES & OBJECTS'''
# Classes are a "Blueprin"t" for a specfic data type.
# A class stores properties and functions called methods.
# We write code programming logic to modify or return the class
# properties.

'''The Strng Class have attributes that is the value of the string 
and method such as lower(), upper(), split() '''

# For example we could represent a class called Student to represent a student
# Set the properties of the student to match those stored in the database 
# such as name, age, etc.

'DEFINING A CLASS IN PYTHON'

class Student(): # This is how you define a class
    def _init_(self, age, name, gender, grades): # This is the 'constructor'
        # Special Type of function that uses 'init' to initialise the different
        # informations as objects that I can pass into the function.
        self.age = age
        self.name = name
        self.gender = gender
        self.grades = grades
# Following the parameter called 'self' that marks the different objects
# in the Student class For instance self.age = 25. Allowing me to create more
# objects that collect the information of the students from their properties.

'CREATING OBJECTS FROM A CLASS'
# Objects are initialised versions of my blueprint

# Create Student Objects
philani = Student(20, "Phulani Sithole", "Male")
sarah = Student(25, "Gower Campbell", "Male")

# Age, name and gender are passed when defining a new object of type student.
# THen we can add some actions to the student class with methods.

'CREATING METHODS FOR A CLASS'
# Method to calculate the average grade
         def compute_average(self)
             average = sum(self.grades)/len(self.grades)
             print("The average for student " + self.name + " is " + str(average))
# Output: The average for student Sarah Jones is 70.


# Method Call
gower.compute_average()
# Only an object of type student can use this method as it is defined for
# the student class. Predefined method.

# Adding a new value to the student attributes, namely grades, which is a
# a list of integets representing a student's grades.

# compute_average is defined under the student class. This method tales self as
# an argument. This method has access to a specific Students object properties.

# Using self.grades & self.name

# The average for student Sarah Jones is 70

# REMBER TO BREAK THINGS UP


'CLASS VARIABLES vs INSTANCE VARIABLES'

'Constructor' # Auto when object created

'Encapsulation' # Bundling related attributues and methods into a structured
# unoit, which also involves restrincting direct access to data

'Self-referencing' # Self is a reference to the current instance of the class
# Allowing methods to access and modify the objects attributes and call other 
# methods within the class.

class Wolf:
     # Class variable
     classification = "canine"

# Create Wolf object
new_wolf = Wolf()

# Print classification (class variable) for new_wolf
print(new_wolf.classification)

# A class named wolf. An attribute of all wolves, the code uses its
# classification to set it too "canine" when we create new_wolf object 
# and create an attribute for that object will be canin. 

class Wolf: 
# class variables
     classification = "canine"
     habitat = "forest"

# constructor nethid with instance variables name and age
     def _init_(self, name, age):
         self.name = name
         self.age = age
# First object, provide instance variables for age constructor

silver_tooth = Wolf("Silvertooth", 5)

#Print out instance variabe 'name'
print(silver_tooth.name)

# print out class variable 'habitat'
print(silver_tooth.habitat)

#Second Object
lone_wolf = Wolf("Lone Wolf", 8)

#Print out instance variable 'name'
print(lone_wolf.name)

#Print out instance variable 'classification'
print(lone_wolf.classification)

'''Creating objects er eliminate the need to declare the values of the 
class variables'''

'CHANGING ATTRIBUTE VALUES FROM INSIDE THE OBJECT'
# From within an object, it is possible to change the attribute values
# when a specfic method has been called.


class Wolf:
     classification = "canine"
     habitat = "forest"
     is_sleeping = False # Defaults to being awkae initially

     def _init(self, name, age):
          self.name = name
          self.age = age

# Method to put wolf to sleep (self needs to be passed as argument so 
# that all of properties are available to thr method

     def bed_time(self):
         self.is_sleeping = True

# Method to wake up wolf (self needs to be passed as argument so  that
# all of the properties are available to the method)
     def wake_up(self):
         self.is_sleeping = False


'CHANGING ATTRIBUTE VALUES FROM OUTSIDE THE OBJECT'

# We can also change the attribute from outside of the object without using 
# methods by using dot notation

class Wolf:
     classification = "canine"
     habitat = "forest"
     is_sleeping = False # Defaults to being awkae initially
          
     # Constructor method with instance variables name and age      
     def _init(self, name, age):
          self.name = name
          self.age = age
    
    # Method that returns the sleep state of the wolf
    def show_sleep_state(self):
        if self.is_sleeeping == False:
             return self.name + " is awake"
        else:
             return self.name + " is sleeeping"
        
# Initialise a wolf object and print the intial sleep 
# state which is awake
silver_tooth = Wolf("Silver Tooth", 6)
print(silver_tooth.show_sleep_state())

# Change sleep state to sleeping using dor notation and then print new state
silver_tooth.is_sleeping = True
print(silver_tooth.show_sleep_state())

# Experiment with this code

"Difference between precedual and object oriented" 
#Object oriented (template, object) For example, name, position salary, 
# active defined.

# Defintion of OOP
# A programming paradigm on the concept of "objects"
# Objecys contain attributes (data) and mbd methods(behavours)
# OOP organizes software design and data or objects rather than functions 
# or logic.

#Encapsulation
#Bundling data & methods that ioerate in that data.
# Hidin internal details and providing a public interfacr

#Inheritance
# Creating new classes based on existing classes
#Promotes code reuse and establishes hierarchy

#Polymorphism
#Objects of different classses can be treated as 
# objects of a common base class
# Allows for flexible and extensible code.

("""Based on a base class; triangle, square, etc. 
 You have different versions of a shape""")

#Abstraction
# Simplifying complex systems by modeling classes based on real world
# entities (methods or processes)
# Focusing on esssential features while hiding unnecessary details.

'Defintion of Class'
#Blueprint for creating obects
#Defines attributes (data: properties or characteristics) 
# and methods (behaviors: functopms or operations)

# Instances are deployments of the above templates


class Car: # Constructor
     def _init_(self, make, model):
     self.make = make # Attributes
     self.model = model

     def display_info(self): # Behaviour
          print(f"this is a {self.make} {self.model}")

#Creating object
my_car = Car("Toyota)", "Corolla")

# A class defines the type of object: Specfifies the data,
# (attributes) objects will hold and the action
# methods/behaviour) they can perform

# Classes organize into real world models

#Onjects is an instance of a class - built from a blueprint/class

'dot operator (.)' # interact with object
#Accessing attributes:
object.attribute # ( e.g., my_dog.name)
# Calling methods: object.method
#my_dog.bark())

# Actions & Behaviour: Methods(function)

'intance methods'
# operates for a specfic object data
# seelf refers to the current object, allowing access and modification 
# of its attributes.

# Example: my_dog.bark() - dit operator bark() method

# 'Class Method' operates on the 'classs itself'
@classmethod decorator #.cls(by convention)
# uses cases: class-level information tracking)
# dog.get_num_dogs() - dot operator calls the class method

'Static Method' (does not inherit the class and attributes)
# Does not need the staticmethod decorator. (No self or cls)
#Use Case: Ultity function logically grouped

"Instance (unique to a variable) vs. Class Attributes(shared in all variables)"

# instance attributes are defined __init__ using self; class attributes 
# are defined at the class level

'Example:'
'my_dog.name(instance),'
'Dog.num_dogs(class)'

"Ecapsulation and Data Hiding"
# - ENCAPSULATION (bundles data (attributes) and methods within a class)

# - Data hiding: restrict direct access to internal data for data integrity.

# _prefix indicates "internal use" (convention, not strict privacy)

# getters(access) and setters(modify) provide controlled access and data 
# validation

'Example my_dog.get_age(), my_dog.set_age(5)'

# Will not be able to access it outside the class

# Classes: Blueprints
# Objects: Instances
#Attributes (instance/Class): Data
#Methods (instance/Class/Static): Actions
# Dot Operator: Accessing attributes and calling methods
# Encapsulation: Data protection

# Abstarction: hiding complex
# Encapsulation (recap) bundling and protecting data
# Modularity: breaking down prograims into self-contained modules (classes)
# Reusablity: Using classes multiple times

# ----- Written by Gower Campbell -----

# ----- Differentiate between class attributes & instance attributes -----
# ----- Explain and use static & class methods -----

# ----- Class - Instance - Object -----
# A class is a blueprint for creating objects
# An instance is a single object created from a class

# ----- 'Class Attributes' -----
# Definition: Class attributes are variables defined within a class, but 
# outside of any methods. They are shared by all instances of the class.

# - Belong to the class, not the individual objects
# - Change affects all instances of the class

class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

# Accessing class attributes
obj1 = MyClass("Instance 1")
print(MyClass.class_attribute)  # Access class attribute
print(obj1.class_attribute)  # Access class attribute through object

# ----- 'Instance Attributes' -----
# Definition: Instance attributes are variables that are bound to a 
# particular instance of a class.

# - Unique to each object
# - Defined within the __init__ method
# - Do not affect other instances of the class

class MyClass:
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

# Creating instances of the class
obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")

# Accessing instance attributes
print(obj1.instance_attribute)  # Access instance attribute
print(obj2.instance_attribute)  # Access instance attribute

# ----- Key Differences -----
# Class attributes are shared across instances, while instance attributes are unique to each object.
#
# Attribute       | Scope            | Access Through   | Shared Instances |
# ----------------|------------------|------------------|------------------|
# Class Attribute | The Entire Class | Class or Instance| Yes              |
# Instance Attrib | Single Object    | Instance Only    | No               |

# ----- 'Instance Methods' -----
# Definition: Instance methods are functions defined within a class and bound to
# an instance of the class. They operate on data (attributes) specific to that
# instance.

# - Access to instance via self parameter
# - Modify instance attributes and return instance-specific information

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, subject):
        return f"{self.name} is studying {subject}"

# Creating an instance of the class
student1 = Student("Alice", 20)
print(student1.study("Mathematics"))  # Output: Alice is studying Mathematics.

# ----- 'Static Methods' -----
# Definition: Static methods do not depend on the class or instance data.
# - Self-contained and perform operations without modifying 
#   class or instance attributes.

# - No access to class or instance
# - Used as utility functions for the class

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    def multiply(self, x):
        self.value *= x

    def __init__(self, initial_value=0):
        self.value = initial_value

# Using the static method
print(Calculator.add(5, 10))  # Output: 15
calc = Calculator(10)
calc.multiply(5)
print(calc.value)  # Output: 50

# ----- 'Class Methods' -----
# Definition: Class Methods operate on the class itself rather than the instances
# of the class. They have access to the class data and can modify class attributes.

# - Often used for methods that create, modify, or delete class attributes.

class MyClass:
    class_attribute = "I am a class attribute"

    @classmethod
    def class_method(cls):
        return cls.class_attribute

# Accessing the class method
print(MyClass.class_method())  # Output: I am a class attribute

# ----- Naming Conventions -----
# - Python classes use CamelCase naming convention
# - Class names should start with a capital letter
# - Method names use lowercase with underscores for readability
# - Class attributes are usually defined at the top of the class
# - Instance attributes are defined within the __init__ method
# - Static methods use the @staticmethod decorator
# - Class methods use the @classmethod decorator
# - Use descriptive names for classes, methods, and attributes
# - Follow PEP 8 guidelines for naming conventions
# - Avoid using reserved keywords as class or method names

class Person:
    """Docstrings: Describe the purpose of the class or method.
    Class representing a person with name, surname, and age."""
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Pet:
    """ A class to represent a pet.
    Class Attributes: name, species, age"""
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

# ----- Practical: Simple Car Management System -----
# Objective: Create a Car class to manage car information. The class should:
# - Keep track of the total number of cars created.
# - Store information about each car (VIN, color, model).
# - Have a default manufacturer but allow it to be changed for all cars.
# - Validate VIN numbers.
# - Display car details.

class Car:
    manufacturer = "Default Manufacturer"
    total_cars = 0

    def __init__(self, vin, color, model):
        self.vin = vin
        self.color = color
        self.model = model
        Car.total_cars += 1

    @classmethod
    def update_manufacturer(cls, new_manufacturer):
        cls.manufacturer = new_manufacturer

    @staticmethod
    def validate_vin(vin):
        return len(vin) == 17 and vin.isalnum()

    def display_details(self):
        return (f"VIN: {self.vin}, Color: {self.color}, Model: {self.model}, "
                f"Manufacturer: {Car.manufacturer}")

# ----- Example Usage -----
car1 = Car("1HGCM82633A123456", "Red", "Civic")
car2 = Car("2T1BURHE0FC123457", "Blue", "Corolla")

print(car1.display_details())
print(car2.display_details())

Car.update_manufacturer("New Manufacturer")
print(car1.display_details())

print(Car.validate_vin("1HGCM82633A123456"))  # Output: True

# ----- Resources & Further Reading -----
# - Think Python, 2nd edition: https://greenteapress.com/wp/think-python-2e/
# - Official Python Documentation: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
# - Real Python Tutorial: https://realpython.com/instance-class-and-static-methods-demystified/
# - Indently YouTube Channel: https://www.youtube.com/watch?v=PIKiHq1O9HQ


# Conclusion
# Class attributes are shared by all instances of a class
# Instance attributes are unique to each object
# Instance methods operate on instance-specific data
# Static methods are self-contained and do not modify class or instance data
# Class methods operate on class data and can modify class attributes

