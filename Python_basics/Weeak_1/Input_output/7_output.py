# Using underscores for large numbers
large_number = 1_000_000
print(f"Large number: {large_number:,}")  # Large number: 1,000,0
# Using f-strings with custom objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
point = Point(3, 4)
print(f"Point: {point}")  # Point: Point(3, 4)
# Advanced formatting with f-strings
number = 1234567.891011
print(f"Number with commas: {number:,.2f}")  # Number with commas: 1,234,567.89
# Using f-strings in function definitions
def greet(name, age):
    return f"Hello, {name}. You are {age} years old."
print(greet("Alice", 30))  # Output: Hello, Alice. You are 30 years old.
# Using f-strings with conditional expressions
score = 85
result = "Pass" if score >= 60 else "Fail"
print(f"Result: {result}")  # Output: Result: Pass
# Using f-strings with list comprehensions
squares = [1, 4, 9, 16, 25]
print(f"Squares: {[x**2 for x in squares]}")  # Squares: [1, 16, 81, 256, 625]
# Using f-strings with generator expressions
even_numbers = (x for x in range(10) if x % 2 == 0)
print(f"Even numbers: {list(even_numbers)}")  # Even numbers: [0, 2, 4, 6, 8]
# Using f-strings with set comprehensions
unique_numbers = {x for x in [1, 2, 2, 3, 4, 4, 5]}
print(f"Unique numbers: {unique_numbers}")  # Unique numbers: {1, 2, 3, 4, 5}
# Using f-strings with dictionary comprehensions
squared_dict = {x: x**2 for x in range(5)}
print(f"Squared dictionary: {squared_dict}")  # Squared dictionary: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# Using f-strings with nested data structures   
data = {"person": {"name": "Alice", "age": 30}, "scores": [85, 90, 95]}
print(f"Name: {data['person']['name']}, Age: {data['person']['age']}")  # Name: Alice, Age: 30
print(f"Scores: {data['scores']}")  # Scores: [85, 90, 95]
# Using f-strings with complex numbers  
complex_num = 3 + 4j
print(f"Complex number: {complex_num.real} + {complex_num.imag}j")  # Complex number: 3.0 + 4.0j
# Using f-strings with bytes        
byte_data = b"Hello"
print(f"Byte data: {byte_data.decode('utf-8')}")  # Byte data: Hello
# Using f-strings with memory views
byte_array = bytearray(b"Hello")
mem_view = memoryview(byte_array)
print(f"Memory view: {mem_view.tobytes().decode('utf-8')}")  # Memory view: Hello
# Using f-strings with exceptions
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  #
    print(f"Error: {e}")  # Output: Error: division by zero
# Using f-strings with logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"Logging an info message with value: {42}")  # Logs: Logging an info message with value: 42        
# Using f-strings with assertions
x = 10      
assert x > 5, f"x should be greater than 5, but got {x}"  # No error
# Using f-strings with type hints   
def add(a: int, b: int) -> int:
    return a + b    
print(f"Sum: {add(3, 4)}")  # Sum: 7
# Using f-strings with dataclasses (Python 3.7+)
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
person = Person("Bob", 25)
print(f"Name: {person.name}, Age: {person.age}")  # Name: Bob, Age: 25