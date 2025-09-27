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
