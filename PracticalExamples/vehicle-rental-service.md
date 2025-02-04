# Vehicle Rental Service with Inheritance

## Introduction

This system manages a fleet of vehicles available for rental. It demonstrates the use of inheritance in Python by creating specialized classes (`Car` and `Bike`) that inherit from a common base class (`Vehicle`). The main purpose is to show how inheritance allows us to extend a base class to create more specific types of vehicles. [Python File Here](vehicle-rental-service.md)

---

## Classes Breakdown

### 1. `Vehicle` Class (Base Class)

The `Vehicle` class is the parent class, containing general attributes and methods common to all types of vehicles.

```python
class Vehicle:
    def __init__(self, type, make, model, daily_rate):
        self.type = type
        self.make = make
        self.model = model
        self.daily_rate = daily_rate
```

- **Attributes**:
  - `type`: The type of vehicle (e.g., car, bike).
  - `make`: The manufacturer of the vehicle.
  - `model`: The model name of the vehicle.
  - `daily_rate`: The daily rental rate for the vehicle.

- **Methods**:
  - `__repr__`: Provides a string representation of the vehicle object.
  - `to_dict`: Converts the vehicle object to a dictionary for JSON serialization.

---

### 2. `Car` Class (Subclass of `Vehicle`)

The `Car` class is a specialized type of `Vehicle`. It inherits from `Vehicle` and adds an extra attribute: `is_convertible` to specify whether the car is a convertible or not.

```python
class Car(Vehicle):
    def __init__(self, make, model, daily_rate, is_convertible=False):
        super().__init__("Car", make, model, daily_rate)
        self.is_convertible = is_convertible
```

- **Inherits**:
  - `Car` inherits all attributes and methods from the `Vehicle` class.
  
- **Additional Attribute**:
  - `is_convertible`: Boolean flag to specify if the car is a convertible.

- **Methods**:
  - `__repr__`: Overrides the `__repr__` method to include the `is_convertible` attribute.
  - `to_dict`: Overrides the `to_dict` method to include the `is_convertible` attribute in the dictionary representation of the object.

---

### 3. `Bike` Class (Subclass of `Vehicle`)

The `Bike` class is another subclass of `Vehicle`. It adds a unique attribute: `has_sidecar` to indicate if the bike has a sidecar.

```python
class Bike(Vehicle):
    def __init__(self, make, model, daily_rate, has_sidecar=False):
        super().__init__("Bike", make, model, daily_rate)
        self.has_sidecar = has_sidecar
```

- **Inherits**:
  - `Bike` inherits all attributes and methods from the `Vehicle` class.

- **Additional Attribute**:
  - `has_sidecar`: Boolean flag to indicate if the bike has a sidecar.

- **Methods**:
  - `__repr__`: Overrides the `__repr__` method to include the `has_sidecar` attribute.
  - `to_dict`: Overrides the `to_dict` method to include the `has_sidecar` attribute in the dictionary.

---

### 4. `VehicleRentalService` Class

The `VehicleRentalService` class manages the fleet of vehicles. It can add, update, list, and calculate rental costs for vehicles. This class can handle both `Car` and `Bike` objects, thanks to inheritance.

```python
class VehicleRentalService:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """Add a new vehicle to the fleet."""
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Only instances of Vehicle or its subclasses can be added.")
        self.vehicles.append(vehicle)
        print(f"Vehicle added: {vehicle}")

    def update_vehicle(self, index, make=None, model=None, daily_rate=None, additional_attributes=None):
        """Update an existing vehicle's details."""
        if index < 0 or index >= len(self.vehicles):
            raise IndexError("Invalid vehicle index.")
        vehicle = self.vehicles[index]
        if make:
            vehicle.make = make
        if model:
            vehicle.model = model
        if daily_rate:
            if not isinstance(daily_rate, (int, float)) or daily_rate <= 0:
                raise ValueError("Daily rate must be a positive number.")
            vehicle.daily_rate = daily_rate
        if additional_attributes:
            if isinstance(vehicle, Car) and 'is_convertible' in additional_attributes:
                vehicle.is_convertible = additional_attributes['is_convertible']
            if isinstance(vehicle, Bike) and 'has_sidecar' in additional_attributes:
                vehicle.has_sidecar = additional_attributes['has_sidecar']
        print(f"Vehicle updated: {vehicle}")

    def list_vehicles(self):
        """List all vehicles in the fleet."""
        if not self.vehicles:
            print("No vehicles found.")
        for i, vehicle in enumerate(self.vehicles):
            print(f"{i + 1}. {vehicle}")
```

- **Methods**:
  - `add_vehicle`: Adds a `Vehicle` (or subclass) to the fleet.
  - `update_vehicle`: Updates an existing vehicle’s attributes, including attributes specific to subclasses (`Car` and `Bike`).
  - `list_vehicles`: Lists all vehicles in the fleet.
  
---

### 5. `main` Function

The `main` function demonstrates how to use the `VehicleRentalService` class. It creates vehicles (`Car` and `Bike`), adds them to the rental service, updates vehicle information, and performs various operations.

```python
def main():
    service = VehicleRentalService()

    # Add vehicles (now using Car and Bike)
    car1 = Car("Toyota", "Corolla", 50, is_convertible=True)
    bike1 = Bike("Yamaha", "YZF-R3", 30, has_sidecar=False)
    service.add_vehicle(car1)
    service.add_vehicle(bike1)

    # List all vehicles
    print("\nAll Vehicles:")
    service.list_vehicles()

    # Update a vehicle (update the convertible status for a Car)
    print("\nUpdating Vehicle 1:")
    service.update_vehicle(0, additional_attributes={'is_convertible': False})

    # Calculate rental cost
    print("\nCalculating Rental Cost for Vehicle 2 (3 days):")
    cost = service.calculate_rental_cost(1, 3)
    print(f"Rental Cost: ${cost}")

    # Export vehicles to a file
    service.export_vehicles("vehicles.json")

    # Import vehicles from a file
    service.import_vehicles("vehicles.json")

if __name__ == "__main__":
    main()
```

- **Key Features**:
  - Add `Car` and `Bike` vehicles to the rental service.
  - List all vehicles in the fleet.
  - Update vehicle attributes (e.g., change `is_convertible`).
  - Calculate rental costs based on daily rate.
  - Export and import vehicle data from a JSON file.

---

## Key Concepts

### 1. **Inheritance**
- The `Car` and `Bike` classes are subclasses of the `Vehicle` class. This means they inherit all the attributes and methods of `Vehicle` but can also introduce their own specialized attributes and methods.
- In this case, `Car` adds the `is_convertible` attribute, while `Bike` adds `has_sidecar`.

### 2. **Method Overriding**
- The `Car` and `Bike` classes override the `__repr__` and `to_dict` methods to provide specialized behavior for these specific vehicle types (adding the new attributes in the output).

### 3. **Polymorphism**
- The `VehicleRentalService` class can interact with both `Car` and `Bike` objects in the same way as `Vehicle` objects, but it can also handle the special attributes for `Car` and `Bike` when updating or displaying vehicle information.

---

## Conclusion

This example shows how inheritance helps in organizing and extending code by creating specialized subclasses (`Car` and `Bike`) while maintaining common functionality in a base class (`Vehicle`). The `VehicleRentalService` class makes use of polymorphism to manage different types of vehicles effectively. 🚗🏍️

```

This breakdown provides a detailed explanation of the code and the concepts of inheritance, method overriding, and polymorphism used in the example. Save it as `vehicle_rental_service.md` for documentation or sharing purposes!
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
   - [CoGrammar Knotes](#cogrammar-knotes)
   - Additional notes and resources provided by CoGrammar for mastering Python and OOP.

---
