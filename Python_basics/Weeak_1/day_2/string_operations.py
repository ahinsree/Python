print("===Basic String Operations===")
text = "Hello Python World"
# 1. convert to uppercase
upper_text = text.upper()
print(f"Uppercase: {upper_text}")
# 2. convert to Lowercase
lower_text = text.lower()
print(f"Lowercase: {lower_text}")
# 3. capitalize the first letter
capitalized_text = text.capitalize()
print(f"capitalized: {capitalized_text}")
# 4.count occurrences of 'o'
count_o = text.count('o')
print(f"count of 'o': {count_o}")
# 5.fing positin of 'Python'
position_python = text.find('Python')
print(f"position of 'python': {position_python}")
# 6.replace 'world' with 'Learners'
replaced_text = text.replace('World','Learners')
print(f"replaced text: {replaced_text}")