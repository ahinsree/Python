"""8. Garbage Collection Process
Diagram 10: Reference Counting"""

"""Memory Diagram: Reference counting and garbage collection

Step 1: a = [1,2,3]    Step 2: b = a    Step 3: del a
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│     a       │ ───┐    │     a       │ ───┐    │     a       │ (deleted)
│             │    │    │             │    │    │             │
├─────────────┤    │    ├─────────────┤    │    ├─────────────┤
│     b       │    │    │     b       │ ───┘    │     b       │ ───┐
└─────────────┘    │    └─────────────┘         └─────────────┘    │
                   │                                               │
                   └──→ list([1,2,3]) ←────────────────────────────┘
                       ref count: 1          ref count: 1

When ref count reaches 0 → Garbage collected!"""

import sys

# Check reference count
a = [1, 2, 3]
print(f"Reference count of a: {sys.getrefcount(a)}")

b = a  # Increase reference count
print(f"Reference count after b = a: {sys.getrefcount(a)}")

del a  # Decrease reference count
print(f"Reference count after del a: {sys.getrefcount(b)}")