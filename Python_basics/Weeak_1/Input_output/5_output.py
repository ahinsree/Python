#Python Output Functions
#Python provides several ways to display output. The most common are print(), but there are also other methods for formatted output.
#Basic print() Function
#Syntax
"""Syntax: print(*objects, sep=' ', end='\n', file=None, flush=False)

*objects: One or more objects to print (converted to strings if not already strings).
sep: Separator between objects (default: single space).
end: String appended after the last object (default: newline \n).
file: Output stream (default: sys.stdout for console).
flush: Forces immediate output (default: False)."""

"""Parameter Breakdown
1. *objects (Positional Arguments)
Required: No, but usually provided

Default: None

Purpose: The values to print. Can be multiple values separated by commas."""

# Single object
print("Hello")                    # Hello

# Multiple objects
print("Hello", "World")           # Hello World
print(1, 2, 3)                   # 1 2 3

# Expressions
print(5 + 3)                     # 8
print(len("Python"))             # 6

"""2. sep (Separator)
Required: No

Default: ' ' (space)

Purpose: Specifies how to separate multiple objects"""

# Default separator (space)
print("Hello", "World")           # Hello World

# Custom separators
print("Hello", "World", sep="-")  # Hello-World
print("2023", "12", "25", sep="/") # 2023/12/25
print("A", "B", "C", sep="")      # ABC
print("Name", "Age", sep=": ")    # Name: Age

# Multi-character separators
print("Python", "Java", "C++", sep=" | ")  # Python | Java | C++

"""3. end (End Character)
Required: No

Default: '\n' (newline)

Purpose: Specifies what to print at the end of the output."""

# Default end (newline)
print("Hello")
print("World")
# Output:
# Hello
# World

# Custom end characters
print("Hello", end=" ")          # No newline, space instead
print("World")                   # Hello World

print("Loading", end="...")      # Loading...
print("Done!")                   # Loading...Done!

print("Item", end=", ")          # Item,
print("Price", end=": ")         # Item, Price: 
print("$10")                     # Item, Price: $10

# Empty end (no newline)
print("No newline", end="")
print(" continues")              # No newline continues

"""4. file (Output Destination)
Required: No

Default: sys.stdout (console)

Purpose: Specifies where to write the output"""

# Writing to a file
with open("output.txt", "w") as f:
    print("Hello File!", file=f)

# Writing to stderr (error stream)
import sys
print("Error message", file=sys.stderr)

# Multiple output destinations
with open("log.txt", "w") as log_file:
    print("Normal message")                    # Goes to console
    print("Log message", file=log_file)        # Goes to file
    
"""5. flush (Buffer Control)
Required: No

Default: False

Purpose: Controls whether to flush the output buffer immediately"""

import time

# Without flushing (default behavior)
print("Processing", end="")
for i in range(3):
    time.sleep(1)
    print(".", end="")  # All dots appear after 3 seconds
print("Done!")

# With flushing
print("Processing", end="", flush=True)
for i in range(3):
    time.sleep(1)
    print(".", end="", flush=True)  # Dots appear one by one
print("Done!")

"""Complete Syntax Examples
Combining All Parameters
print(*objects, sep=' ', end='\n', file=None, flush=False)"""

# Complex print statement
name = "Alice"
age = 25
score = 95.5

print("Student:", name, "Age:", age, "Score:", score, 
      sep=" | ", 
      end=" --- END\n", 
      flush=True)
# Output: Student: | Alice | Age: | 25 | Score: | 95.5 --- END


# Basic printing
print("Hello, World!")  # Output: Hello, World!
# Printing multiple items
print("Hello", "World","!")  # Output: Hello,World,!
# With custom separator
print("04", "12", "1993", sep="-")  # Output: 04-12-1993")
# Without newline
print("Loading", end="...")  # Output: Loading...
print("Done!") # Output: Done!
# With new line
print("Loading", end="\n")  # Output: Loading
print("Done!") # Output: Done!
# printing variables
name = "Alice"
age = 30
print("Name:", name, "Age:", age)  # Output: Name: Alice Age: 30
# Formatted Strings (f-strings)
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30
# Using format() method
print("Name: {}, Age: {}".format(name, age))  # Output: Name: Alice, Age: 30
# Using % operator
print("Name: %s, Age: %d" % (name, age))  # Output: Name: Alice, Age: 30
# Printing to a file
with open("output.txt", "w") as file:
    print("Hello, File!", file=file)  # Output will be written to output.txt
# Advanced Formatting
number = 123.456789
print(f"Number: {number:.2f}")  # Output: Number: 123.46
print(f"Number: {number:10.2f}")  # Output: Number:     123.46 (width 10)
print(f"Number: {number:<10.2f}")  # Output: Number: 123.46    (left-aligned)
print(f"Number: {number:^10.2f}")  # Output: Number:   123.46   (centered)
# Escape Sequences  
print("Line1\nLine2")  # Output: Line1 (new line) Line2
print("Column1\tColumn2")  # Output: Column1 (tab) Column2
print("He said, \"Hello!\"")  # Output: He said, "Hello!"
print('It\'s a sunny day!')  # Output: It's a sunny day!
print("C:\\Users\\Name")  # Output: C:\Users\Name
# Raw Strings
print(r"C:\Users\Name")  # Output: C:\Users\Name
# Summary
# The print() function is versatile and can be customized for various output needs. It supports multiple arguments, custom separators, and formatted strings for better readability. Additionally, Python provides various  ways to format output, making it easy to present data in a user-friendly manner.
# For more complex output formatting, consider using libraries like PrettyTable, tabulate, or logging for structured logging output.
