#Best Practices
#Good Variable Names

# Descriptive names
user_age = 25  # Good
ua = 25        # Bad - not descriptive

# Consistent naming style
first_name = "John"    # snake_case (Python convention)
lastName = "Doe"       # camelCase (not Python convention)

# Meaningful names
is_logged_in = True    # Good
flag = True            # Bad - not meaningful
#Variable Reusability
# Reusing variables appropriately
score = 0
score = score + 10  # Good - incremental update
print(f"Score: {score}")

# vs creating new variables unnecessarily
new_score = score + 10  # Less optimal - unnecessary new variable
print(f"New Score: {new_score}")

#Advanced Variable Techniques
#Unpacking Sequences
# Tuple unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"X: {x}, Y: {y}, Z: {z}")

# List unpacking
colors = ["red", "green", "blue"]
primary, secondary, tertiary = colors

# Extended unpacking
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

#Variable Annotations (Python 3.6+)
# Type hints (optional but helpful)
name: str = "Alice"
age: int = 25
scores: list[int] = [85, 92, 78]
is_student: bool = True

def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
"""Key Points to Remember
Variables don't need type declaration - Python infers types automatically

Use descriptive names - makes code more readable

Follow naming conventions - snake_case for variables, UPPER_CASE for constants

Variables are references to objects - not the objects themselves

Understand variable scope - local vs global variables

Variables are fundamental to programming in Python - they allow you to store, manipulate, and reference data throughout your programs!"""