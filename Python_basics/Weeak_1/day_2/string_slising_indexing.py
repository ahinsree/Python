print("===STRING SLICING AND INDEXING===")
text = "Python programming is amazing"
# 1. get first six characters 
first_six = text[:6]
print(f"first six characters:'{first_six}'")
# 2. get last seven characters
last_seven = text[-7:]
print(f"last seven characters:'{last_seven}'")
# 3. get characters from index 7 to 17
middle = text[7:18]
print(f"characters from index 7 to 17:'{middle}'")
# 4. get every second character
every_second = text[::2]
print(f"every seond character:'{every_second}")
# 5.Reverse the string
reversed_text = text[::-1]
print(f"reversed string:'{reversed_text}'")
# 6. get first word using split
word = text.split()
first_word = word[0]
print(f"first word: {first_word}")

