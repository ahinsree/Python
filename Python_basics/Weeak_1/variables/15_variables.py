"""7. Function Call Memory Model
Diagram 9: Function Local Variables"""

"""Memory Diagram: Function call with parameters

Global Scope            Function Scope (temp)
┌─────────────┐         ┌─────────────┐
│   x = 10    │         │   param = 10 │
│   y = 20    │         │   temp = 30  │
└─────────────┘         └─────────────┘
         │                     │
         └─────────────────────┘ (pass by reference)

Function parameters become new references to same objects"""

def modify_number(num):
    print(f"Inside function - num id: {id(num)}")
    num += 5  # Creates new object for immutable types
    print(f"After modification - num id: {id(num)}")
    return num

x = 10
print(f"Before function - x id: {id(x)}")
result = modify_number(x)
print(f"After function - x id: {id(x)}")  # Unchanged
print(f"Result id: {id(result)}")  # Different from original x