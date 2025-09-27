"""9. Complete Memory Flow Example
Diagram 11: Complete Program Flow"""

"""Python Program Execution Memory Flow:

Code:                    Memory State:
x = 10                   Stack: x → Heap: int(10) id: 1000
y = x                    Stack: x, y → Heap: int(10) id: 1000
z = [1, 2]               Stack: x, y, z → Heap: list([1,2]) id: 2000
y = 20                   Stack: x, y, z → Heap: int(20) id: 3000
                         (y now points to new object)
del x                    Stack: y, z → Heap: int(10) ref count 0 → GC"""

#Python Code with Memory Tracking:

def track_memory_changes():
    print("=== Memory Tracking ===")
    
    x = 10
    print(f"Step 1 - x=10: id(x)={id(x)}")
    
    y = x  # Same object
    print(f"Step 2 - y=x: id(y)={id(y)}, x is y: {x is y}")
    
    z = [1, 2]  # New object
    print(f"Step 3 - z=[1,2]: id(z)={id(z)}")
    
    y = 20  # y now references new object
    print(f"Step 4 - y=20: id(y)={id(y)}, x is y: {x is y}")
    
    del x  # Remove reference
    print("Step 5 - del x: x is deleted")

track_memory_changes()

"""Key Points Illustrated:

Variables are references (arrows pointing to objects)

Multiple variables can reference the same object

Immutable objects may be shared (interning)

Mutable objects are always distinct

Function calls create new references

Garbage collection happens when reference count reaches 0

id() shows the memory address of the referenced object"""