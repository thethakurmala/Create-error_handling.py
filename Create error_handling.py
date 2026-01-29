"""
TASK 9: Exception Handling & Logging
"""

import logging

# Configure logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    """Function to divide two numbers with exception handling"""
    try:
        result = a / b

    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        print("Error: Cannot divide by zero")

    except TypeError:
        logging.error("Invalid data type used for division")
        print("Error: Invalid input type")

    else:
        print("Result:", result)

    finally:
        print("Division operation completed")


# Simulating runtime errors
print("---- Exception Handling Demo ----")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    divide_numbers(num1, num2)

except ValueError:
    logging.error("User entered non-integer value")
    print("Error: Please enter valid integers")

finally:
    print("Program execution finished")
