import json

# Base class Vehicle
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

# Derived class Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, daily_rate, is_convertible=False):
        super().__init__("Car", make, model, daily_rate)
        self.is_convertible = is_convertible

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, daily_rate={self.daily_rate}, convertible={self.is_convertible})"

    def to_dict(self):
        # Include the convertible attribute in the dictionary
        data = super().to_dict()
        data["is_convertible"] = self.is_convertible
        return data

# Derived class Bike inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, make, model, daily_rate, has_sidecar=False):
        super().__init__("Bike", make, model, daily_rate)
        self.has_sidecar = has_sidecar

    def __repr__(self):
        return f"Bike(make={self.make}, model={self.model}, daily_rate={self.daily_rate}, sidecar={self.has_sidecar})"

    def to_dict(self):
        # Include the sidecar attribute in the dictionary
        data = super().to_dict()
        data["has_sidecar"] = self.has_sidecar
        return data

# VehicleRentalService that uses Vehicle or its subclasses
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
