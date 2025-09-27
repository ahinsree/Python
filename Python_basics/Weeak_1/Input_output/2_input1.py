# String input
text = input("Enter some text: ")
print(f"You entered: {text}")

# Integer input
age = int(input("Enter your age: "))
print(f"Your age is: {age}")

# Float input
height = float(input("Enter your height in meters: "))
print(f"Your height is: {height} meters")

# Multiple inputs
name, age, height = input("Enter your name, age, and height separated by spaces: ").split()
print(f"Name: {name}, Age: {age}, Height: {height} meters")