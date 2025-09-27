"""4. Mutable vs Immutable Objects
Diagram 4: Immutable Objects (Strings)"""

"""Memory Diagram: s1 = "hello"; s2 = "hello"

Stack (Variables)        Heap (Objects)
┌─────────────┐         ┌─────────────┐
│     s1      │ ──────→ │  str("hello") │
├─────────────┤         │   id: 5000    │
│     s2      │ ──────→ └─────────────┘

String interning: Same string literals share memory location"""

"""Diagram 5: Mutable Objects (Lists)"""

"""Memory Diagram: list1 = [1,2,3]; list2 = [1,2,3]

Stack (Variables)        Heap (Objects)
┌─────────────┐         ┌─────────────┐
│    list1    │ ──────→ │  list([1,2,3]) │
├─────────────┤         │    id: 6000    │
│    list2    │ ──────→ │  list([1,2,3]) │
│             │         │    id: 7000    │
└─────────────┘         └─────────────┘

Mutable objects always create new instances!"""

# Immutable - same object
s1 = "hello"
s2 = "hello"
print(f"Strings - s1 is s2: {s1 is s2}")  # True

# Mutable - different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"Lists - list1 is list2: {list1 is list2}")  # False