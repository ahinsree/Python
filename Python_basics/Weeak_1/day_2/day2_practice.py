# day2 practice.py
print("🎯 DAY2: DATA TYPES AND OPERATIONS")
print("="*40)

# Let's explore different data types in python
print("1. STRING EXPLORATION")
name = "Python learner"
print(f"Name:{name}")
print(f"Type:{type(name)}")
print(f"Uppercase:{name.upper()}")
print(f"Length:{len(name)} characters")
print("\n2.NUMBER EXPLORATION")
age = 31 
temperature =36.6
print(f"Age:{age},Type:{type(age)}")
print(f"Temperature:{temperature},Type:{type(temperature)}")
print("\n 3.BOOLEAN EXPLANATION")
is_beginner = True
has_exprienced = False
print(f"is bignner:{is_beginner},Type:{type(is_beginner)}")
print(f"has exprieanced:{has_exprienced},Type:{type(has_exprienced)}")
# Your turn: create a your own variable
print("\n 4.YOUR VARIABLE")
your_name ="Ahinsree"
your_age = 31
your_city ="Padanilam"
print(f'My Name is:{your_name}')
print(f"I'm {your_age} years old")
print(f"I live in {your_city}")
print("\n"+"="*40)
print("5. MATHAMATICAL OPERATIONS")
a = 15
b =4
print("Basic Math Operations")
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ** {b} = {a**b}")
#Your turn: calculate Your birth year.
current_year = 2025
birth_year = current_year - your_age
print(f"\n if you're {your_age}, you were born in {birth_year}")
# more calculations
print("\n 6. Comparison operators")
print(f"{a} > {b} : {a>b}")
print(f"{a} < {b} : {a<b}")
print(f"{a} >= {b} : {a>=b}")
print(f"{a} <= {b} : {a<=b}")
print(f"{a} == {b} : {a==b}")
print(f"{a} != {b}: {a!=b}")