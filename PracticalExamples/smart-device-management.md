# **1. Class Definition: `SmartDevice`**

The class `SmartDevice` models smart devices with attributes like name, type, location, wattage, power status, and an automatically generated device ID. It provides several methods to interact with these devices and track their status.

---

### **2. Class Attributes:**
```python
connected_devices = 0
total_consumption = 0
```
- **`connected_devices`**: This keeps track of the total number of devices created (this value is shared among all instances of the class).
- **`total_consumption`**: This keeps track of the total power consumption (in watts) of all devices.

---

### **3. Instance Attributes:**
```python
self.name = name
self.device_type = device_type
self.location = location
self.wattage = wattage
self.__power_status = False  # Private attribute
self.id = SmartDevice.register_device()  # Device ID assigned upon creation
```
- **`self.name`**: The name of the device.
- **`self.device_type`**: The type of the device (e.g., Light, Plug, Thermostat).
- **`self.location`**: The location of the device (e.g., Living Room, Kitchen).
- **`self.wattage`**: The power consumption of the device (in watts).
- **`self.__power_status`**: A private attribute that stores the power status of the device (whether it's ON or OFF).
- **`self.id`**: A unique identifier assigned to the device (generated when the device is registered).

---

### **4. Constructor (`__init__`)**

The constructor initializes the device's attributes and automatically registers the device upon creation using the `register_device()` class method.

---

### **5. Instance Methods:**

#### **`turn_on`**
```python
def turn_on(self):
    if not self.__power_status:
        self.__power_status = True
        SmartDevice.update_consumption(self.wattage)
        print(f"{self.name} turned ON")
```
- **Purpose**: Turns the device ON.
- **Logic**: If the device is not already ON (`self.__power_status` is `False`), it sets the power status to `True` (ON), and updates the total power consumption using the `update_consumption()` method with the device's wattage.

#### **`turn_off`**
```python
def turn_off(self):
    if self.__power_status:
        self.__power_status = False
        SmartDevice.update_consumption(-self.wattage)
        print(f"{self.name} turned OFF")
```
- **Purpose**: Turns the device OFF.
- **Logic**: If the device is currently ON (`self.__power_status` is `True`), it sets the power status to `False` (OFF) and reduces the total power consumption by the device's wattage.

#### **`get_power_status`**
```python
def get_power_status(self):
    return self.__power_status
```
- **Purpose**: Returns the current power status of the device (ON or OFF).

---

### **6. Class Methods:**

#### **`register_device`**
```python
@classmethod
def register_device(cls):
    cls.connected_devices += 1
    print(f"Device registered. Total devices: {cls.connected_devices}")
    return cls.connected_devices
```
- **Purpose**: Registers a new device and increments the total number of connected devices.
- **Logic**: Every time a new device is created, this method increments the `connected_devices` class attribute and returns the current number of devices.

#### **`update_consumption`**
```python
@classmethod
def update_consumption(cls, wattage_change):
    cls.total_consumption += wattage_change
    print(f"Updated total power consumption: {cls.total_consumption}W")
    return cls.total_consumption
```
- **Purpose**: Updates the total power consumption based on the change in wattage (either turning a device on or off).
- **Logic**: Adds or subtracts the wattage change to/from the `total_consumption` class attribute and prints the updated value.

---

### **7. Static Method:**

#### **`convert_celcius_fahrenheit`**
```python
@staticmethod
def convert_celcius_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
```
- **Purpose**: Converts a temperature from Celsius to Fahrenheit.
- **Logic**: It takes a Celsius temperature and applies the formula to convert it to Fahrenheit.

---

### **8. Display Method (`display_device_info`)**
```python
def display_device_info(self):
    print(f"Device Name: {self.name}")
    print(f"Device Type: {self.device_type}")
    print(f"Location: {self.location}")
    print(f"Wattage: {self.wattage}W")
    print(f"Power Status: {'ON' if self.__power_status else 'OFF'}")
    print(f"Device ID: {self.id}")
```
- **Purpose**: Prints the details of the device in a readable format.
- **Logic**: Displays the device name, type, location, wattage, power status (ON or OFF), and the unique device ID.

---

### **9. Testing the Functionality**

Below, I created several devices and tested their functionalities, such as turning them on and off, checking power status, and performing a temperature conversion.

```python
living_room_light = SmartDevice("LivingRoom Light", "Light", "Living Room", 10)
kitchen_thermostat = SmartDevice("Kitchen Thermostat", "Thermostat", "Kitchen", 0)
bedroom_plug = SmartDevice("Bedroom Plug", "Plug", "Bedroom", 100)
bedroom_plug_1 = SmartDevice("Bedroom Plug 1", "Plug", "Bedroom", 100)
```
- These are instances of `SmartDevice` representing different devices in different locations with their respective wattage.

```python
living_room_light.turn_on()
living_room_light.turn_off()
living_room_light.turn_on()
```
- Here, the `turn_on` and `turn_off` methods are tested on the `living_room_light` device.

```python
print(f"{kitchen_thermostat.name} Power Status: {kitchen_thermostat.get_power_status()}")
```
- The power status of the `kitchen_thermostat` device is checked using the `get_power_status()` method.

```python
celsius = 37
fahrenheit = SmartDevice.convert_celcius_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")
```
- A static method `convert_celcius_fahrenheit` is used to convert Celsius to Fahrenheit.

---

### **10. Output Example**
```
Device registered. Total devices: 1
Device registered. Total devices: 2
Device registered. Total devices: 3
Device registered. Total devices: 4
Device Name: LivingRoom Light
Device Type: Light
Location: Living Room
Wattage: 10W
Power Status: OFF
Device ID: 1

Device Name: Kitchen Thermostat
Device Type: Thermostat
Location: Kitchen
Wattage: 0W
Power Status: OFF
Device ID: 2

LivingRoom Light turned ON
LivingRoom Light turned OFF
LivingRoom Light is already ON

Kitchen Thermostat Power Status: False

37°C is equal to 98.6°F
```

---

### **11. Summary**

- **Device Management**: The class `SmartDevice` allows for the creation, control, and management of smart devices in different locations with associated power consumption.
- **Class & Instance Methods**: The class uses both instance methods (e.g., `turn_on`, `turn_off`) and class methods (e.g., `register_device`, `update_consumption`) to manage device states and track total power usage.
- **Static Method**: The class also provides a static method for temperature conversion (Celsius to Fahrenheit).
- **Power Consumption Tracking**: The total power consumption is dynamically updated as devices are turned on or off.

This class provides a solid framework for managing smart devices and their attributes while keeping track of overall device statistics like power consumption and device count.

---

This breakdown should give a clear understanding of the functionality and how each part of the code interacts with others! Let me know if you need further clarifications. 😊
