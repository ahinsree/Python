#Advanced Output Examples
#Formatted Strings (f-strings) - Python 3.6+
# Basic f-strings
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30
# Expressions in f-strings
a, b = 5, 10
print(f"{a} + {b} = {a + b}")  # Output: 5 + 10 = 15    
# Formatting numbers
price = 19.9876
print(f"Price: ${price:.2f}")  # Price: $19.99
pi = 3.14159
print(f"Pi: {pi:.2f}")  # Pi: 3.14
percentage = 0.756
print(f"Completion: {percentage:.1%}")  # Completion: 75.6%
# Alignment and padding
text = "Python"
print(f"|{text:<10}|")  # Left align: |Python    |
print(f"|{text:^10}|")  # Center align: |  Python  |
print(f"|{text:>10}|")  # Right align: |    Python|
# Padding numbers
number = 42
print(f"|{number:05}|")  # Pad with zeros: |00042|  
print(f"|{number:>5}|")   # Right align: |   42|
print(f"|{number:<5}|")   # Left align: |42   |
# Date and time formatting
from datetime import datetime
date = datetime(2023, 3, 15, 14, 30)
print(f"Date: {date:%Y-%m-%d}")  # Date: 2023-03-15
print(f"Time: {date:%H:%M}")     # Time: 14:30
print(f"Full: {date:%Y-%m-%d %H:%M}")  # Full: 2023-03-15 14:30
# Nested f-strings
value = 7.12345
print(f"Value rounded: {f'{value:.2f}'}")  # Value rounded: 7.12
# Using f-strings with dictionaries 
person = {"name": "Bob", "age": 25}
print(f"Name: {person['name']}, Age: {person['age']}")  # Name: Bob, Age: 25
# Using f-strings with lists
fruits = ["apple", "banana", "cherry"]
print(f"First fruit: {fruits[0]}")  # First fruit: apple
# Multiline f-strings
multiline = f"""This is a multiline
f-string example."""
print(multiline)  # Output: This is a multiline f-string example.
# Combining different formatting options
value = 123.456789  
print(f"Value: {value:>10.2f}")  # Value:     123.46
print(f"Value: {value:<10.2f}")  # Value: 123.46    
print(f"Value: {value:^10.2f}")  # Value:   123.46
