"""3. Integer Interning (-5 to 256)
Diagram 3: Integer Interning"""

"""Memory Diagram: x = 100; y = 100; z = 1000; w = 1000

Stack (Variables)        Heap (Objects)
┌─────────────┐         ┌─────────────┐
│     x       │ ──────→ │   int(100)  │ ←──┐
├─────────────┤         │   id: 3000  │    │
│     y       │ ──────→ └─────────────┘    │
├─────────────┤                            │ Same object
│     z       │ ──────→ ┌─────────────┐    │ (interning)
├─────────────┤         │  int(1000)  │    │
│     w       │ ──────→ │  id: 4000   │ ←──┘
└─────────────┘         └─────────────┘

Small integers (-5 to 256) are cached and reused!"""
# Small integers (interning works)
x = 100
y = 100
print(f"x is y: {x is y}")  # True - same object

# Large integers (no interning)
z = 1000
w = 1000
print(f"z is w: {z is w}")  # Usually False (implementation dependent)