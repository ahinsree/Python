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