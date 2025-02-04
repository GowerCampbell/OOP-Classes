# Employee Onboarding System

This document provides an overview of the **Employee Onboarding System**, designed to manage employee details, perform string manipulations, handle employee hobbies, process weekly sales data, and interact with dictionaries for storing employee data. 

---

## **Code Breakdown**

### **1. String Manipulation**

In the first section, string manipulation is performed to manage employee names and format the display of employee information.

#### **Functions**:
- **`create_full_name`**: Concatenates first name and last name to form the employee's full name.
- **`get_initials`**: Extracts the initials from the employee's first name and last name.
- **`display_employee_data`**: Displays the employee's data in a tabular format using the `tabulate` module.

```python
def create_full_name(first_name, last_name):
    """Concatenate first name and last name to form the full name."""
    return first_name + " " + last_name

def get_initials(first_name, last_name):
    """Extract initials from the first and last name."""
    return first_name[0] + last_name[0]

def display_employee_data(full_name, age, department, hobbies, sales):
    """Display employee data in a clean tabular format using tabulate."""
    employee_data = [
        ["Full Name:", full_name],
        ["Age:", age],
        ["Department:", department],
        ["Hobbies:", ", ".join(hobbies)],
    ]
    
    # Print employee data in table format
    print("Employee Data:")
    print(tabulate(employee_data, tablefmt="plain"))
    
    # Display weekly sales data
    print("\nSales Data (Weekly Sales):")
    sales_headers = ["Week", "Sales"]
    weekly_sales = [
        [f"Week {i+1}", sum(week)]  # Summing up sales for each week
        for i, week in enumerate(sales)
    ]
    print(tabulate(weekly_sales, headers=sales_headers, tablefmt="grid"))
```

### **2. List Operations**

In this section, we handle employee hobbies and weekly sales data. We perform various operations like adding/removing hobbies and calculating total and average sales for the employee.

#### **Functions**:
- **`add_hobby`**: Adds a new hobby to the list.
- **`remove_hobby`**: Removes a hobby from the list.
- **`display_hobbies`**: Displays the employee's hobbies.
- **`calculate_total_sales`**: Calculates the total sales from the weekly sales data.
- **`calculate_average_sales`**: Calculates the average sales for each week.

```python
def add_hobby(hobbies, new_hobby):
    """Add a new hobby to the hobbies list."""
    hobbies.append(new_hobby)
    return hobbies

def remove_hobby(hobbies, hobby):
    """Remove a hobby from the hobbies list."""
    if hobby in hobbies:
        hobbies.remove(hobby)
    return hobbies

def display_hobbies(hobbies):
    """Display the list of hobbies."""
    print("Employee Hobbies:", hobbies)

def calculate_total_sales(weekly_sales):
    """Calculate total sales for all weeks."""
    return sum(sum(week) for week in weekly_sales)

def calculate_average_sales(weekly_sales):
    """Calculate the average sales for each week."""
    return [sum(week) / len(week) for week in weekly_sales]
```

### **3. Dictionary Operations**

This section handles the employee information using a dictionary to store and manage various details. We can update, fetch, and display employee information.

#### **Functions**:
- **`create_employee`**: Creates an employee dictionary with details like name, age, department, hobbies, and sales data.
- **`update_employee_info`**: Updates a specific key-value pair in the employee's dictionary.
- **`display_employee_info`**: Displays the employee's full dictionary.
- **`get_employee_info`**: Fetches a specific value from the employee's dictionary.
- **`display_employee_items`**: Displays all key-value pairs of the employee's dictionary.
- **`display_employee_keys`**: Displays all the keys in the employee's dictionary.
- **`display_employee_values`**: Displays all the values in the employee's dictionary.

```python
def create_employee(first_name, last_name, age, department, address, hobbies, sales):
    """Create a dictionary for storing employee details including sales data."""
    full_name = create_full_name(first_name, last_name)
    employee = {
        'name': full_name,
        'age': age,
        'department': department,
        'address': address,
        'hobbies': hobbies,
        'sales': sales  # Added sales data
    }
    return employee

def update_employee_info(employee, key, value):
    """Update a specific key-value pair in the employee dictionary."""
    employee[key] = value
    return employee

def display_employee_info(employee):
    """Display the employee's dictionary information."""
    print(f"** Employee Details:\n{employee}")

def get_employee_info(employee, key):
    """Fetch a specific value from the employee dictionary."""
    return employee.get(key)

def display_employee_items(employee):
    """Display all key-value pairs in the employee dictionary."""
    print("Employee Items:", employee.items())

def display_employee_keys(employee):
    """Display all keys of the employee dictionary."""
    print("Employee Keys:", employee.keys())

def display_employee_values(employee):
    """Display all values of the employee dictionary."""
    print("Employee Values:", employee.values())
```

### **4. Main Function**

The `main` function manages the entire workflow of the employee onboarding system. It initializes hobbies, weekly sales data, performs string manipulations, and manages employee data using dictionaries.

#### **Steps**:
1. Initialize a list of hobbies and weekly sales data.
2. Add/remove hobbies and display them.
3. Create the employee's full name and initials.
4. Create an employee dictionary and display all employee data.
5. Perform sales-related calculations (total and average sales).
6. Update employee details (department and address).
7. Fetch specific employee data and display keys, values, and items.

```python
def main():
    # Print output header
    print("========= Employee Onboarding ========\n")
    
    # Initialise hobbies list and weekly sales data
    hobbies = ['reading', 'travelling', 'cycling', 'cooking']
    weekly_sales = [
        [100, 200, 150],  # Week 1
        [250, 300, 200],  # Week 2
        [300, 400, 350]   # Week 3
    ]
    
    # Adding and removing hobbies
    hobbies = add_hobby(hobbies, 'painting')
    display_hobbies(hobbies)
    hobbies = remove_hobby(hobbies, 'cooking')
    display_hobbies(hobbies)
    
    # Create full name, initials, and employee data display
    first_name = "John"
    last_name = "Doe"
    full_name = create_full_name(first_name, last_name)
    initials = get_initials(first_name, last_name)
    print(f"Full Name: {full_name}")
    print(f"Initials: {initials}\n")
    
    # Create employee with sales data
    employee = create_employee(first_name, last_name, 30, 'HR', 
                                '123 Elm Street', hobbies, weekly_sales)
    display_employee_data(full_name, 30, 'HR', hobbies, weekly_sales)
    
    # Perform sales-related calculations
    total_sales = calculate_total_sales(employee['sales'])
    print(f"Total Sales for All Weeks: {total_sales}")
    
    average_sales = calculate_average_sales(employee['sales'])
    for i, avg_sales in enumerate(average_sales, 1):
        print(f"Average Sales for Week {i}: {avg_sales}")
    
    # Update employee department and address
    employee = update_employee_info(employee, 'department', 'Sales')
    employee = update_employee_info(employee, 'address', '456 Oak Street')
    display_employee_info(employee)
    
    # Get specific employee data
    employee_age = get_employee_info(employee, 'age')
    print(f"Employee Age: {employee_age}")
    
    # Display employee keys, values, and items
    display_employee_items(employee)
    display_employee_keys(employee)
    display_employee_values(employee)

# Run the main function to execute the onboarding system
if __name__ == "__main__":
    main()
```

---

## **Enhancements and Possible Improvements**

- **Data Persistence**: Implement functionality to save employee data to a file and load it back on program start.
- **Employee Search**: Add the ability to search for employees based on specific criteria like department or age.
- **User Interface**: A more interactive user interface (UI) can be created for better interaction with the system.

---

## **Final Thoughts**

This Employee Onboarding System effectively handles various tasks using Python's string, list, and dictionary operations. The system can be extended to support more features like handling multiple employees, advanced search options, and data persistence.
