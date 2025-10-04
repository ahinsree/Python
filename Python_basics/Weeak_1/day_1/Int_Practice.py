while True:
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Factorial undefined for negatives!")
            again = input("Do you want to calculate again? (yes/no): ")
            if again.lower() != "yes":
                break
            continue
        # Calculate factorial using loop
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        print(f"The factorial of {number} is {fact}")
        again = input("Do you want to calculate again? (yes/no): ")
        if again.lower() != "yes":
            break
    except ValueError:
        print("Invalid input! Please enter whole numbers only.")