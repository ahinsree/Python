print("🧮Simple_calculator")
print("="*20 )
# get input from user
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
# perform calculations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined ( cannot divide by zero)"
foloordivision = num1 // num2 if num2 != 0 else "undefined ( cannot divide by zero)"
modulus = num1 % num2 if num2 != 0 else "undefined ( cannot divide by zero)"
exponentiation = num1 ** num2
#display results
print(f"sum: {sum}")
print(f"difference: {difference}")
print(f"product: {product}")
print(f"division: {division}")
print(f"folardivision: {foloordivision}")
print(f"moculus: {modulus}")
print(f"exponentiation: {exponentiation}")
