# Car Management System

This system allows you to manage a collection of cars, including adding, updating, searching, and exporting/importing car data. It is built using Python and follows Object-Oriented Programming (OOP) principles.

---

## Table of Contents

1. **[Features](#features)**
2. **[Code Implementation](#code-implementation)**
   - [Car Class](#car-class)
   - [CarManager Class](#carmanager-class)
   - [Example Usage](#example-usage)
3. **[Key Improvements](#key-improvements)**
4. **[Reflection](#reflection)**
5. **[Bibliography](#bibliography)**

---

## Features

1. **Add a Car**: Add a new car with make, model, and year.
2. **Update Car Details**: Modify the make, model, or year of an existing car.
3. **Search for Cars**: Find cars by make, model, or year.
4. **List All Cars**: Display all cars in the system.
5. **Export Cars to File**: Save car data to a file.
6. **Import Cars from File**: Load car data from a file.

---

## Code Implementation

### Car Class

The `Car` class represents a car object with attributes `make`, `model`, and `year`. It includes methods for converting the object to a dictionary and a string representation.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, year={self.year})"

    def to_dict(self):
        """Convert car object to a dictionary for JSON serialization."""
        return {"make": self.make, "model": self.model, "year": self.year}
```

---

### CarManager Class

The `CarManager` class manages a collection of cars. It includes methods for adding, updating, searching, listing, exporting, and importing cars.

```python
import json

class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self, make, model, year):
        """Add a new car to the system."""
        if not make or not model or not year:
            raise ValueError("Make, model, and year are required.")
        if not isinstance(year, int) or year < 1900 or year > 2023:
            raise ValueError("Year must be a valid integer between 1900 and 2023.")
        car = Car(make, model, year)
        self.cars.append(car)
        print(f"Car added: {car}")

    def update_car(self, index, make=None, model=None, year=None):
        """Update an existing car's details."""
        if index < 0 or index >= len(self.cars):
            raise IndexError("Invalid car index.")
        car = self.cars[index]
        if make:
            car.make = make
        if model:
            car.model = model
        if year:
            if not isinstance(year, int) or year < 1900 or year > 2023:
                raise ValueError("Year must be a valid integer between 1900 and 2023.")
            car.year = year
        print(f"Car updated: {car}")

    def search_cars(self, make=None, model=None, year=None):
        """Search for cars by make, model, or year."""
        results = []
        for car in self.cars:
            if (make and car.make.lower() == make.lower()) or \
               (model and car.model.lower() == model.lower()) or \
               (year and car.year == year):
                results.append(car)
        return results

    def list_cars(self):
        """List all cars in the system."""
        if not self.cars:
            print("No cars found.")
        for i, car in enumerate(self.cars):
            print(f"{i + 1}. {car}")

    def export_cars(self, filename):
        """Export car data to a JSON file."""
        car_data = [car.to_dict() for car in self.cars]
        with open(filename, "w") as file:
            json.dump(car_data, file, indent=4)
        print(f"Car data exported to {filename}.")

    def import_cars(self, filename):
        """Import car data from a JSON file."""
        with open(filename, "r") as file:
            car_data = json.load(file)
        self.cars = [Car(**data) for data in car_data]
        print(f"Car data imported from {filename}.")
```

---

### Example Usage

```python
def main():
    manager = CarManager()

    # Add cars
    manager.add_car("Toyota", "Corolla", 2020)
    manager.add_car("Honda", "Civic", 2018)
    manager.add_car("Ford", "Mustang", 2022)

    # List all cars
    print("\nAll Cars:")
    manager.list_cars()

    # Update a car
    print("\nUpdating Car 1:")
    manager.update_car(0, make="Toyota", model="Camry", year=2021)

    # Search for cars
    print("\nSearch Results for 'Toyota':")
    results = manager.search_cars(make="Toyota")
    for car in results:
        print(car)

    # Export cars to a file
    manager.export_cars("cars.json")

    # Import cars from a file
    manager.import_cars("cars.json")

if __name__ == "__main__":
    main()
```

---

## Key Improvements

1. **Input Validation**:
   - Ensures that `make`, `model`, and `year` are provided when adding a car.
   - Validates that `year` is a valid integer between 1900 and 2023.

2. **Dynamic Updates**:
   - Allows updating individual attributes (make, model, or year) of a car without overwriting the entire object.

3. **Error Handling**:
   - Raises `ValueError` for invalid inputs and `IndexError` for invalid car indices.

4. **Search Functionality**:
   - Searches for cars by `make`, `model`, or `year` (case-insensitive for strings).

5. **Export/Import**:
   - Exports car data to a JSON file for persistence.
   - Imports car data from a JSON file to restore the system state.

---

## Reflection

This project was an excellent opportunity to apply Object-Oriented Programming (OOP) principles in Python. By creating the `Car` and `CarManager` classes, I was able to encapsulate car-related data and behaviors into reusable components. The system is modular, making it easy to extend with additional features in the future.

One of the challenges I faced was ensuring robust input validation and error handling. For example, validating the `year` attribute required careful consideration of edge cases, such as invalid integers or out-of-range values. Implementing the search functionality also required thoughtful design to ensure it was both efficient and user-friendly.

The export/import feature was particularly rewarding to implement. It demonstrates how data persistence can be achieved using JSON files, which are both human-readable and widely supported. This feature makes the system more practical for real-world use.

Overall, this project deepened my understanding of OOP, file handling, and error management in Python. It also highlighted the importance of designing systems with scalability and usability in mind.

---

## Bibliography

1. **Python Documentation**:
   - [Python Official Documentation](https://docs.python.org/3/)
   - Provides comprehensive information on Python syntax, libraries, and best practices.

2. **Real Python**:
   - [Real Python Tutorials](https://realpython.com/)
   - Offers in-depth tutorials on Python programming, including OOP and file handling.

3. **GeeksforGeeks**:
   - [GeeksforGeeks Python Articles](https://www.geeksforgeeks.org/python-programming-language/)
   - A valuable resource for learning Python concepts and solving coding problems.

4. **JSON Documentation**:
   - [JSON.org](https://www.json.org/)
   - Explains the JSON format and its use in data interchange.

5. **CoGrammar Knotes**:
   - [CoGrammar Knotes](/knotes.py)
   - Additional notes and resources provided by CoGrammar for mastering Python and OOP.

---

This breakdown, reflection, and bibliography provide a complete overview of the Car Management System, its implementation, and the learning outcomes. 🚗✨
