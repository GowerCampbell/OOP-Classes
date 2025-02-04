
# Special Methods (Magic/Dunder Methods)

Special methods, also known as **magic methods** or **dunder methods** (double underscore methods), are predefined methods in Python that allow you to define how objects of a class behave in specific situations. They are automatically invoked by Python in response to certain operations.

---

## **1. Constructors and Destructors**

### **`__init__` (Constructor)**
The `__init__` method is called when an object is created. It is used to initialize the object's attributes.

#### Example:
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating an object
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.make)  # Output: Toyota
```

---

### **`__del__` (Destructor)**
The `__del__` method is called when an object is about to be destroyed. It is used for cleanup operations, such as closing files or releasing resources.

#### Example:
```python
class FileManager:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print(f"Opened {filename}")

    def __del__(self):
        self.file.close()
        print("File closed.")

# Creating an object
file_manager = FileManager("example.txt")
file_manager.file.write("Hello, World!")
# When the object is destroyed, __del__ is called, closing the file.
```

---

## **2. String Representation**

### **`__repr__`**
The `__repr__` method returns an official string representation of an object, primarily used for debugging and development. It should include detailed information about the object's state.

#### Example:
```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Student(name={self.name!r}, id={self.student_id!r})"

# Creating an object
student = Student("Alice", "A123")
print(repr(student))  # Output: Student(name='Alice', id='A123')
```

---

### **`__str__`**
The `__str__` method returns a user-friendly string representation of an object. It is called by the `print()` function and `str()`.

#### Example:
```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Student Name: {self.name}, ID: {self.student_id}"

# Creating an object
student = Student("Bob", "B456")
print(student)  # Output: Student Name: Bob, ID: B456
```

---

## **3. Container-Like Objects**

### **`__len__`**
The `__len__` method returns the length of the container. It is called by the `len()` function.

#### Example:
```python
class MyList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

# Creating an object
my_list = MyList()
my_list.add(10)
my_list.add(20)

print(len(my_list))  # Output: 2
```

---

### **`__getitem__`**
The `__getitem__` method allows indexing into the container. It is called when you use square brackets (`[]`) to access an item.

#### Example:
```python
class MyList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]

# Creating an object
my_list = MyList()
my_list.add(10)
my_list.add(20)

print(my_list[0])  # Output: 10
```

---

## **4. Comparators**

### **`__eq__` (Equality)**
The `__eq__` method defines the behavior of the `==` operator.

#### Example:
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

# Creating objects
student1 = Student("Alice", 85)
student2 = Student("Bob", 85)

print(student1 == student2)  # Output: True
```

---

### **`__lt__` (Less Than)**
The `__lt__` method defines the behavior of the `<` operator.

#### Example:
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __lt__(self, other):
        return self.grade < other.grade

# Creating objects
student1 = Student("Alice", 85)
student2 = Student("Bob", 90)

print(student1 < student2)  # Output: True
```

---

### **`__gt__` (Greater Than)**
The `__gt__` method defines the behavior of the `>` operator.

#### Example:
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __gt__(self, other):
        return self.grade > other.grade

# Creating objects
student1 = Student("Alice", 85)
student2 = Student("Bob", 90)

print(student1 > student2)  # Output: False
```

---

### **Common Comparator Methods**
- `x == y` → `__eq__(self, other)`
- `x != y` → `__ne__(self, other)`
- `x < y` → `__lt__(self, other)`
- `x <= y` → `__le__(self, other)`
- `x > y` → `__gt__(self, other)`
- `x >= y` → `__ge__(self, other)`

---
