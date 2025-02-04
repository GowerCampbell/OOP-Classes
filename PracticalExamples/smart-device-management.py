class SmartDevice:
    # Class attributes
    connected_devices = 0
    total_consumption = 0

    # Constructor (Initialization of object attributes)
    def __init__(self, name, device_type, location, wattage=0):
        self.name = name
        self.device_type = device_type
        self.location = location
        self.wattage = wattage
        self.__power_status = False  # Initially, the device is OFF (private)
        self.id = SmartDevice.register_device()  # Register the device upon creation

    # Turn the device ON (Instance method(Inherits attributes))
    def turn_on(self):
        if not self.__power_status:
            self.__power_status = True
            SmartDevice.update_consumption(self.wattage)
            print(f"{self.name} turned ON")

    # Turn the device ON (Instance method)
    # def turn_on(self):
    #     if not self.power_status:  # Only turn on if it's off
    #         self.power_status = True
    #         SmartDevice.update_consumption(self.wattage)
    #         print(f"{self.name} turned ON")

   # Turn the device OFF (Instance method)
    def turn_off(self):
        if self.__power_status:
            self.__power_status = False
            SmartDevice.update_consumption(-self.wattage)
            print(f"{self.name} turned OFF")
# Getter for private attribute __power_status
    def get_power_status(self):
        return self.__power_status

    # Class method to register a new device
    @classmethod
    def register_device(cls):
        cls.connected_devices += 1
        print(f"Device registered. Total devices: {cls.connected_devices}")
        return cls.connected_devices

    # Class method to update the total power consumption
    # Triggered within the class
    @classmethod 
    def update_consumption(cls, wattage_change):
        cls.total_consumption += wattage_change
        print(f"Updated total power consumption: {cls.total_consumption}W")
        return cls.connected_devices

    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def convert_celcius_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


# Instantiate SmartDevice objects
living_room_light = SmartDevice("LivingRoom Light", "Light", "Living Room", 10)
kitchen_thermostat = SmartDevice("Kitchen Thermostat", "Thermostat", "Kitchen", 0)
bedroom_plug = SmartDevice("Bedroom Plug", "Plug", "Bedroom", 100)
bedroom_plug_1 = SmartDevice("Bedroom Plug 1", "Plug", "Bedroom", 100)

# Test the functionality
print("\n--- Device Information ---")
print(f"Connected Devices: {living_room_light.connected_devices}")  # Access shared attribute
print(f"{kitchen_thermostat.name}, ID: {kitchen_thermostat.id}")

print("\n--- Device Operations ---")
living_room_light.turn_on()  # Turn ON the LivingRoom Light
living_room_light.turn_off()  # Turn OFF the LivingRoom Light
living_room_light.turn_on()  # Try turning it ON again

# Check power status using getter
print("\n--- Checking Power Status ---")
print(f"{kitchen_thermostat.name} Power Status: {kitchen_thermostat.get_power_status()}")

# Test static method
print("\n--- Celsius to Fahrenheit Conversion ---")
celsius = 37
fahrenheit = SmartDevice.convert_celcius_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")

if __name__ == "__main__":
    main()
