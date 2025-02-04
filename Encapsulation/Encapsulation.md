# **Encapsulation**
   - [Private Attributes](#Private-Attributes)
   - [Getter and Setter Methods](#Getter-and-Setter-Methods)

Encapsulation is one of the four fundamental principles of Object-Oriented Programming (OOP). It refers to bundling data (attributes) and methods (functions) that operate on the data into a single unit (a class). It also involves restricting direct access to some of an object's components, which is achieved using **private attributes** and **getter/setter methods**.

---

### **Private Attributes**
In Python, there’s no strict concept of "private" attributes like in some other languages (e.g., Java). However, Python uses a naming convention to indicate that an attribute or method should be treated as private.

- **Naming Convention**: Prefix an attribute or method name with an underscore (`_`) to indicate it’s intended to be private.
- **Name Mangling**: Prefix an attribute or method name with double underscores (`__`) to make it harder to access directly (Python internally changes the name to `_ClassName__attribute`).

#### Example:
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute
        self.__balance = balance  # Private attribute (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount.")

# Creating an object
account = BankAccount("Alice", 1000)

# Accessing public attribute
print(account.owner)  # Output: Alice

# Trying to access private attribute directly (will raise an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing private attribute using name mangling (not recommended)
print(account._BankAccount__balance)  # Output: 1000 (but don't do this!)

# Using methods to interact with private attributes
account.deposit(500)  # Output: Deposited $500. New balance: $1500
account.withdraw(200)  # Output: Withdrew $200. New balance: $1300
```

---

### **Getter and Setter Methods**
Since private attributes aren’t directly accessible, we use **getter** and **setter** methods to control access to them. This allows us to add validation or logic when getting or setting the value of an attribute.

#### Example:
```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        if isinstance(name, str) and name.strip() != "":
            self.__name = name.strip()
        else:
            print("Invalid name.")

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 120:
            self.__age = age
        else:
            print("Invalid age.")

# Creating an object
person = Person("John", 25)

# Using getter methods
print(person.get_name())  # Output: John
print(person.get_age())   # Output: 25

# Using setter methods
person.set_name("Jane")
person.set_age(30)

print(person.get_name())  # Output: Jane
print(person.get_age())   # Output: 30

# Trying to set invalid values
person.set_name("")       # Output: Invalid name.
person.set_age(150)       # Output: Invalid age.
```

---

### **Why Use Getters and Setters?**
1. **Control Access**: You can restrict how attributes are accessed or modified.
2. **Validation**: You can add checks to ensure the data is valid before setting it.
3. **Read-Only or Write-Only Attributes**: You can make attributes read-only or write-only by omitting the setter or getter.

---

### **Using Properties for Better Encapsulation**
Python provides a cleaner way to implement getters and setters using the `@property` decorator. This allows you to access methods as if they were attributes.

#### Example:
```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius  # Private attribute

    # Getter for celsius (accessed like an attribute)
    @property
    def celsius(self):
        return self.__celsius

    # Setter for celsius (accessed like an attribute)
    @celsius.setter
    def celsius(self, value):
        if -273.15 <= value <= 1000:
            self.__celsius = value
        else:
            print("Invalid temperature.")

    # Getter for fahrenheit (computed property)
    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

# Creating an object
temp = Temperature(25)

# Accessing celsius as an attribute
print(temp.celsius)  # Output: 25

# Setting celsius as an attribute
temp.celsius = 30
print(temp.celsius)  # Output: 30

# Accessing fahrenheit (computed property)
print(temp.fahrenheit)  # Output: 86.0

# Trying to set invalid temperature
temp.celsius = -300  # Output: Invalid temperature.
```

---

### **Key Takeaways**
1. **Private Attributes**: Use a single underscore (`_`) or double underscores (`__`) to indicate private attributes.
2. **Getters and Setters**: Use methods or properties to control access to private attributes.
3. **Properties**: Use the `@property` decorator for a cleaner and more Pythonic way to implement getters and setters.

