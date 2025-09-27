"""6. Nested Objects and References
Diagram 8: Nested List Structure"""

"""Memory Diagram: matrix = [[1,2], [3,4]]

Stack (Variables)        Heap (Objects)
┌─────────────┐         ┌─────────────┐
│   matrix    │ ──────→ │  list(ref1)  │ id: 11000
├─────────────┤         ├─────────────┤
│             │         │  ref1 ──────→ list([1,2]) id: 12000
│             │         │  ref2 ──────→ list([3,4]) id: 13000
└─────────────┘         └─────────────┘

Nested structure with multiple reference levels"""

matrix = [[1, 2], [3, 4]]
print(f"matrix id: {id(matrix)}")
print(f"matrix[0] id: {id(matrix[0])}")
print(f"matrix[1] id: {id(matrix[1])}")

# Modifying inner list
matrix[0].append(99)
print(f"Modified matrix: {matrix}")  # [[1, 2, 99], [3, 4]]