"""5. Reference Assignment vs Copy
Diagram 6: Reference Assignment vs Copy
In Python, variables are references to objects in memory. When you assign one variable to another,"""

"""Memory Diagram: original = [1,2,3]; reference = original

Stack (Variables)        Heap (Objects)
┌─────────────┐         ┌─────────────┐
│  original   │ ──────→ │ list([1,2,3]) │
├─────────────┤         │   id: 8000    │
│  reference  │ ──────→ └─────────────┘
└─────────────┘

Both variables point to SAME list object!
Modifying through either variable affects both! the new variable points to the same object. This is called reference assignment. If you want to create a copy of the object instead, you can use methods like slicing or the copy module."""

#"""Diagram 7: Creating a Copy"""
"""Memory Diagram: original = [1,2,3]; copy = original.copy()

Stack (Variables)        Heap (Objects)
┌─────────────┐         ┌─────────────┐
│  original   │ ──────→ │ list([1,2,3]) │
├─────────────┤         │   id: 9000    │
│    copy     │ ──────→ │ list([1,2,3]) │
│             │         │   id: 10000   │
└─────────────┘         └─────────────┘

Different objects! Modifying one doesn't affect the other."""

# Reference assignment
original = [1, 2, 3]
reference = original  # Same object
reference.append(4)
print(f"Original after reference mod: {original}")  # [1, 2, 3, 4]

# Copy
original = [1, 2, 3]
copy_list = original.copy()  # Different object
copy_list.append(4)
print(f"Original after copy mod: {original}")  # [1, 2, 3] - unchanged