# Vehicle Rental Service

This system allows you to manage a fleet of vehicles for rental, including cars and bikes. It calculates rental costs based on the number of days rented and supports adding, updating, searching, and exporting/importing vehicle data.

---

## Features

1. **Add a Vehicle**: Add a new vehicle with type, make, model, and daily rental rate.
2. **Update Vehicle Details**: Modify the make, model, or daily rental rate of an existing vehicle.
3. **Search for Vehicles**: Find vehicles by type, make, or model.
4. **List All Vehicles**: Display all vehicles in the system.
5. **Calculate Rental Cost**: Calculate the rental cost for a specific vehicle based on the number of days.
6. **Export Vehicles to File**: Save vehicle data to a file.
7. **Import Vehicles from File**: Load vehicle data from a file.

---

## Code Implementation

### Vehicle Class

The `Vehicle` class represents a vehicle object with attributes `type`, `make`, `model`, and `daily_rate`. It includes methods for converting the object to a dictionary and a string representation.

```python
class Vehicle:
    def __init__(self, type, make, model, daily_rate):
        self.type = type
        self.make = make
        self.model = model
        self.daily_rate = daily_rate

    def __repr__(self):
        return f"Vehicle(type={self.type}, make={self.make}, model={self.model}, daily_rate={self.daily_rate})"

    def to_dict(self):
        """Convert vehicle object to a dictionary for JSON serialization."""
        return {
            "type": self.type,
            "make": self.make,
            "model": self.model,
            "daily_rate": self.daily_rate,
        }
```

---

### VehicleRentalService Class

The `VehicleRentalService` class manages a fleet of vehicles. It includes methods for adding, updating, searching, listing, calculating rental costs, exporting, and importing vehicles.

```python
import json

class VehicleRentalService:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, type, make, model, daily_rate):
        """Add a new vehicle to the fleet."""
        if not type or not make or not model or not daily_rate:
            raise ValueError("Type, make, model, and daily rate are required.")
        if not isinstance(daily_rate, (int, float)) or daily_rate <= 0:
            raise ValueError("Daily rate must be a positive number.")
        vehicle = Vehicle(type, make, model, daily_rate)
        self.vehicles.append(vehicle)
        print(f"Vehicle added: {vehicle}")

    def update_vehicle(self, index, type=None, make=None, model=None, daily_rate=None):
        """Update an existing vehicle's details."""
        if index < 0 or index >= len(self.vehicles):
            raise IndexError("Invalid vehicle index.")
        vehicle = self.vehicles[index]
        if type:
            vehicle.type = type
        if make:
            vehicle.make = make
        if model:
            vehicle.model = model
        if daily_rate:
            if not isinstance(daily_rate, (int, float)) or daily_rate <= 0:
                raise ValueError("Daily rate must be a positive number.")
            vehicle.daily_rate = daily_rate
        print(f"Vehicle updated: {vehicle}")

    def search_vehicles(self, type=None, make=None, model=None):
        """Search for vehicles by type, make, or model."""
        results = []
        for vehicle in self.vehicles:
            if (type and vehicle.type.lower() == type.lower()) or \
               (make and vehicle.make.lower() == make.lower()) or \
               (model and vehicle.model.lower() == model.lower()):
                results.append(vehicle)
        return results

    def list_vehicles(self):
        """List all vehicles in the fleet."""
        if not self.vehicles:
            print("No vehicles found.")
        for i, vehicle in enumerate(self.vehicles):
            print(f"{i + 1}. {vehicle}")

    def calculate_rental_cost(self, index, days):
        """Calculate the rental cost for a specific vehicle."""
        if index < 0 or index >= len(self.vehicles):
            raise IndexError("Invalid vehicle index.")
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Number of days must be a positive integer.")
        vehicle = self.vehicles[index]
        return vehicle.daily_rate * days

    def export_vehicles(self, filename):
        """Export vehicle data to a JSON file."""
        vehicle_data = [vehicle.to_dict() for vehicle in self.vehicles]
        with open(filename, "w") as file:
            json.dump(vehicle_data, file, indent=4)
        print(f"Vehicle data exported to {filename}.")

    def import_vehicles(self, filename):
        """Import vehicle data from a JSON file."""
        with open(filename, "r") as file:
            vehicle_data = json.load(file)
        self.vehicles = [Vehicle(**data) for data in vehicle_data]
        print(f"Vehicle data imported from {filename}.")
```

---

### Example Usage

```python
def main():
    service = VehicleRentalService()

    # Add vehicles
    service.add_vehicle("Car", "Toyota", "Corolla", 50)
    service.add_vehicle("Bike", "Yamaha", "YZF-R3", 30)
    service.add_vehicle("Car", "Ford", "Mustang", 100)

    # List all vehicles
    print("\nAll Vehicles:")
    service.list_vehicles()

    # Update a vehicle
    print("\nUpdating Vehicle 1:")
    service.update_vehicle(0, type="Car", make="Toyota", model="Camry", daily_rate=60)

    # Search for vehicles
    print("\nSearch Results for 'Car':")
    results = service.search_vehicles(type="Car")
    for vehicle in results:
        print(vehicle)

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

---

## Key Improvements

1. **Input Validation**:
   - Ensures that `type`, `make`, `model`, and `daily_rate` are provided when adding a vehicle.
   - Validates that `daily_rate` is a positive number.

2. **Dynamic Updates**:
   - Allows updating individual attributes (type, make, model, or daily rate) of a vehicle without overwriting the entire object.

3. **Error Handling**:
   - Raises `ValueError` for invalid inputs and `IndexError` for invalid vehicle indices.

4. **Search Functionality**:
   - Searches for vehicles by `type`, `make`, or `model` (case-insensitive for strings).

5. **Rental Cost Calculation**:
   - Calculates the rental cost based on the number of days and the vehicle's daily rate.

6. **Export/Import**:
   - Exports vehicle data to a JSON file for persistence.
   - Imports vehicle data from a JSON file to restore the system state.

---

## Reflection

This project was an excellent opportunity to apply Object-Oriented Programming (OOP) principles in Python. By creating the `Vehicle` and `VehicleRentalService` classes, I was able to encapsulate vehicle-related data and behaviors into reusable components. The system is modular, making it easy to extend with additional features in the future.

One of the challenges I faced was ensuring robust input validation and error handling. For example, validating the `daily_rate` attribute required careful consideration of edge cases, such as non-numeric or negative values. Implementing the search functionality also required thoughtful design to ensure it was both efficient and user-friendly.

The rental cost calculation feature was particularly rewarding to implement. It demonstrates how business logic can be integrated into a system to provide practical functionality. The export/import feature adds persistence, making the system more practical for real-world use.

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
