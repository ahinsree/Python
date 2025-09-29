print("===STRING VALIDATION===")
def analyze_string(text):
    print(f"\nAnalyzing: '{text}'")
    #check if all alphabetic
    print(f"All alphabetic: {text.isalpha()}")
    #check if all numaric
    print(f"All numaric: {text.isdigit()}")
    #check  if alpha numaric
    print(f"Alphanumaric: {text.isalnum()}")
    #check if all uppercase
    print(f"All uppercase: {text.isupper()}")
    #check if all lowercase
    print(f"All lowercase: {text.islower()}")
    #check if title case
    print(f"Titele case: {text.istitle()}")
    #check if start with specific text
    print(f"starts with 'py': {text.startswith('Py')}")
    #cgeck if end with specific text
    print(f"end with 'ing': {text.endswith('ing')}")
analyze_string("Python123")
analyze_string("HELLO")
analyze_string("hello world")
analyze_string("12345")
analyze_string("Python Programming")
        