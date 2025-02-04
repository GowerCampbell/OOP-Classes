import json

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

# Example Usage
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
