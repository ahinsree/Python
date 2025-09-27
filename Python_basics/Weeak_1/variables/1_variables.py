#Variables in Python
#Variables are used to store data values in Python. They act as containers for storing information that can be referenced and manipulated in your programs.
#Basic Variable Syntax
#variable_name = value

"""Variable Naming Rules
Must start with a letter (a-z, A-Z) or underscore (_)

Can contain letters, numbers, and underscores

Cannot contain spaces or special characters

Case-sensitive (age, Age, and AGE are different variables)

Cannot use Python keywords (if, for, while, etc.) as variable names"""
#Valid Variable Names:
name = "John"
_age = 25
user_name = "john_doe"
count2 = 10
MAX_SIZE = 100
#Invalid Variable Names:
"""2name = "John"      # Starts with number
user-name = "John"  # Contains hyphen
class = "Python"    # Python keyword"""

"""1. Basic Variable Assignment
Diagram 1: Simple Variable Assignment"""

# When you assign a value
x = 10
# Python:
# 1. Creates an integer object with value 10 in memory
# 2. Creates a variable 'x' that references that object
"""Memory Diagram: x = 10

Stack (Variables)        Heap (Objects)
┌─────────────┐         ┌─────────────┐
│   Variable  │         │   Object    │
├─────────────┤         ├─────────────┤
│     x       │ ──────→ │    int(10)  │
│   (ref)     │         │   id: 1000  │
└─────────────┘         └─────────────┘

Explanation:
- Variable 'x' is created in stack
- Integer object 10 is created in heap
- 'x' contains a reference (pointer) to the object in heap"""

#Python Code Demonstration:
x = 10
print(f"x = {x}")
print(f"id(x) = {id(x)}")  # Memory address
print(f"x is at memory location: {hex(id(x))}")

#2. Memory Allocation Process
#Object Creation and Assignment
# Example 1: Simple assignment
a = 100
# Memory process:
# 1. Python checks if integer 100 already exists
# 2. If not, creates new integer object in memory
# 3. Variable 'a' becomes a reference to that object

# Example 2: Multiple references
b = a
# Now both 'a' and 'b' reference the same object in memory

"""2. Multiple References to Same Object
Diagram 2: Shared References"""
# Memory Diagram: a = 100, b = a
"""Memory Diagram: a = 100; b = a

Stack (Variables)        Heap (Objects)
┌─────────────┐         ┌─────────────┐
│   Variable  │         │   Object    │
├─────────────┤         ├─────────────┤
│     a       │ ──────→ │   int(100)  │
│   (ref)     │         │   id: 2000  │
├─────────────┤         └─────────────┘
│     b       │ ──────→ 
│   (ref)     │
└─────────────┘

Both 'a' and 'b' point to the same object!"""

a = 100
b = a  # b references the same object as a

print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"a is b: {a is b}")  # True - same object

"""3. Demonstrating Memory Behavior
Identity and References"""

# Using id() to see memory address
x = 10
y = 10
z = 20

print(f"id(x): {id(x)}")  # Memory address of object x references
print(f"id(y): {id(y)}")  # Same as id(x) due to interning
print(f"id(z): {id(z)}")  # Different address

print(f"x is y: {x is y}")  # True - same object
print(f"x is z: {x is z}")  # False - different objects

"""Mutable vs Immutable Objects"""
# Immutable objects (cannot be changed)
a = 10
b = 10
print(f"a is b: {a is b}")  # True - same object due to interning

# Mutable objects (can be changed)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 is list2: {list1 is list2}")  # False - different objects

"""4. Detailed Memory Storage Examples
Integer Storage"""

# Small integers (-5 to 256) are interned (cached)
a = 100
b = 100
print(f"a is b: {a is b}")  # True - same object

# Large integers are not interned
c = 1000
d = 1000
print(f"c is d: {c is d}")  # False - different objects (usually)

"""String Storage"""

# String interning
s1 = "hello"
s2 = "hello"
print(f"s1 is s2: {s1 is s2}")  # True - same object

# Non-interned strings
s3 = "hello world!"
s4 = "hello world!"
print(f"s3 is s4: {s3 is s4}")  # False - different objects

"""List Storage (Mutable)"""

# Lists are always separate objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # Reference assignment

print(f"list1 is list2: {list1 is list2}")  # False
print(f"list1 is list3: {list1 is list3}")  # True

# Modifying through reference
list3.append(4)
print(f"list1: {list1}")  # [1, 2, 3, 4] - modified!
print(f"list2: {list2}")  # [1, 2, 3] - unchanged

"""5. Memory Management Techniques
Garbage Collection"""
import gc

# Reference counting example
x = [1, 2, 3]  # Reference count = 1
y = x          # Reference count = 2
z = x          # Reference count = 3

del y          # Reference count = 2
z = None       # Reference count = 1
# When reference count reaches 0, memory is freed

# Force garbage collection
gc.collect()

"""Circular References"""

# Circular reference example
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create circular reference
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Circular reference!

# These objects won't be freed by reference counting alone
# Python's garbage collector detects and collects circular references

"""6. Practical Memory Monitoring
Checking Memory Usage"""

import sys

def show_memory_usage(*variables):
    for var in variables:
        print(f"{var} size: {sys.getsizeof(var)} bytes")

# Example usage
x = 10
y = "Hello World"
z = [1, 2, 3, 4, 5]

show_memory_usage(x, y, z)

"""Memory Profiling Example"""

import sys

# Track memory usage of different data types
data_types = [
    10,                    # integer
    3.14159,               # float
    "Hello Python",        # string
    [1, 2, 3, 4, 5],      # list
    (1, 2, 3, 4, 5),      # tuple
    {1, 2, 3, 4, 5},      # set
    {'a': 1, 'b': 2}      # dictionary
]

print("Memory usage by data type:")
for item in data_types:
    print(f"{type(item).__name__:>10}: {sys.getsizeof(item):>4} bytes")
    
"""7. Advanced Memory Concepts
Shallow vs Deep Copy"""

import copy

# Original list with nested list
original = [1, 2, [3, 4]]

# Shallow copy
shallow = copy.copy(original)
shallow[2][0] = 999  # Affects original!
print(f"Original: {original}")  # [1, 2, [999, 4]]

# Deep copy
original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)
deep[2][0] = 999  # Does NOT affect original
print(f"Original: {original}")  # [1, 2, [3, 4]]

"""Memory Optimization with Slots"""

# Regular class (uses dict for attributes)
class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory optimized class
class OptimizedClass:
    __slots__ = ['x', 'y']  # Prevents dict creation
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory comparison
regular = RegularClass(1, 2)
optimized = OptimizedClass(1, 2)

print(f"Regular class size: {sys.getsizeof(regular)} bytes")
print(f"Optimized class size: {sys.getsizeof(optimized)} bytes")

"""8. Real-world Memory Patterns
Efficient Data Storage"""

# Memory-efficient ways to store data

# Instead of list of individual items
numbers_list = [1, 2, 3, 4, 5]  # More memory

# Use array for homogeneous data
import array
numbers_array = array.array('i', [1, 2, 3, 4, 5])  # Less memory

# Generator expressions (memory efficient)
numbers_gen = (x for x in range(1000000))  # Doesn't store all values

"""Memory Management in Functions"""
def process_data():
    large_list = list(range(1000000))  # Large object created
    
    # Process data...
    result = sum(large_list)
    
    # Explicit cleanup
    del large_list  # Helps garbage collector
    gc.collect()
    
    return result

# Function calls create new local namespaces
def test_function():
    x = 10  # Local variable
    print(f"Local x id: {id(x)}")

x = 20  # Global variable
print(f"Global x id: {id(x)}")
test_function()
print(f"Global x unchanged: {x}")

"""9. Memory Visualization"""
# Visualizing variable relationships
def visualize_references():
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    
    print("Memory Relationships:")
    print(f"a = {a}, id: {id(a)}")
    print(f"b = {b}, id: {id(b)} → references same object as a")
    print(f"c = {c}, id: {id(c)} → different object")
    print(f"a is b: {a is b}")  # True
    print(f"a is c: {a is c}")  # False

visualize_references()

"""Key Concepts Summary
Variables are references to objects in memory

Immutable objects (ints, strings, tuples) may be shared/reused

Mutable objects (lists, dicts, sets) are never shared automatically

Memory is managed through reference counting + garbage collection

id() function shows memory address of referenced object

is operator checks if two variables reference the same object

sys.getsizeof() shows memory usage of an object"""

#Memory Optimization Tips

# 1. Use generators for large sequences
def large_sequence():
    return (x * 2 for x in range(1000000))  # Generator expression

# 2. Delete unused variables
large_data = [x for x in range(1000000)]
# Process data...
del large_data  # Free memory when done

# 3. Use appropriate data structures
from collections import namedtuple

# Instead of dictionary
Point = namedtuple('Point', ['x', 'y'])  # More memory efficient
p = Point(10, 20)