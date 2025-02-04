# **Advanced Topics**
- [Lambda Functions and Functional Programming](#lambda-functions-and-functional-programming)
   - [What are Lambda Functions?](#what-are-lambda-functions)
   - [Functional Programming Concepts](#functional-programming-concepts)
   - [Practical Examples](#practical-examples)

- [Decorators](#decorators)
   - [What are Decorators?](#what-are-decorators)
   - [Creating Custom Decorators](#creating-custom-decorators)
   - [Practical Examples](#practical-examples-1)

This section covers **Lambda Functions and Functional Programming** as well as **Decorators**. These concepts allow you to write **cleaner**, **shorter**, and **more efficient** Python code.

---


## 1. Lambda Functions and Functional Programming

### What are Lambda Functions?
Lambda functions are **anonymous**, **one-liner** functions that you can use when you don't want to create a full function with the `def` keyword. They are useful when you need a function for a short period of time.

#### Syntax:
```python
lambda arguments: expression
```

#### Example:
```python
# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

print(add(2, 3))         # Output: 5
print(add_lambda(2, 3))  # Output: 5
```

---

### Functional Programming Concepts
Functional programming is a paradigm where you focus on using **pure functions**, which do not change state and produce the same result for the same input. It also encourages using **higher-order functions**—functions that accept other functions as parameters or return them.

#### Key Concepts:
- **Pure Functions**: No side effects, always the same output for the same input.
- **Higher-Order Functions**: Functions that take or return other functions.
- **Map, Filter, Reduce**: Built-in functions to process sequences in a functional way.

#### Example: Using `map`, `filter`, and `reduce`
```python
from functools import reduce

# Map: Apply a function to each item in a sequence
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Filter: Keep only items that satisfy a condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Reduce: Combine items into a single result (e.g., sum)
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Output: 15
```

---

### Practical Examples

#### Sorting with Lambda
```python
# Sort a list of tuples by the second element
data = [(1, 3), (4, 1), (2, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(4, 1), (2, 2), (1, 3)]
```

#### Custom Sorting
```python
# Sort a list of strings by their length
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['date', 'apple', 'cherry', 'banana']
```

---

## 2. Decorators

### What are Decorators?
Decorators are **functions that modify the behavior** of other functions. They allow you to add functionality to existing functions (like logging, timing, or access control) without changing their code.

#### Syntax:
```python
@decorator
def function():
    pass
```

#### Example:
```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function is called.
# Hello!
# After the function is called.
```

---

### Creating Custom Decorators

#### Decorator with Arguments
```python
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

#### Timer Decorator
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()
# Output: slow_function took 2.0002 seconds to run.
```

---

### Practical Examples

#### Logging Decorator
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logger
def add(x, y):
    return x + y

add(3, 5)
# Output:
# Calling add with args: (3, 5), kwargs: {}
# add returned: 8
```

#### Access Control Decorator
```python
def admin_required(func):
    def wrapper(user, *args, **kwargs):
        if user == "admin":
            return func(user, *args, **kwargs)
        else:
            raise PermissionError("Only admin can access this function.")
    return wrapper

@admin_required
def delete_user(user):
    print(f"User deleted by {user}.")

delete_user("admin")  # Output: User deleted by admin.
delete_user("user")   # Raises PermissionError
```

---

## Reflection

- **Lambda Functions** are useful for short, anonymous functions that can be passed directly into places like `map`, `filter`, or `sorted`.
- **Functional Programming** allows you to write cleaner, more declarative code by focusing on **pure functions** and higher-order functions.
- **Decorators** allow you to extend existing functions without changing their code, which is perfect for adding common features like logging, access control, and performance tracking.

By mastering these advanced topics, I'll be able to write **more modular**, **cleaner**, and **maintainable** Python code! 🚀

---

## Bibliography
- **Python Documentation**: [Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions), [Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- **Real Python**: [Lambda Functions](https://realpython.com/python-lambda/), [Decorators](https://realpython.com/primer-on-python-decorators/)
- **GeeksforGeeks**: [Lambda Functions](https://www.geeksforgeeks.org/python-lambda/), [Decorators](https://www.geeksforgeeks.org/decorators-in-python/)
