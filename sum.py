# Program: Calculate the Sum of Two Numbers

def calculateTheSum():
    # Step 1: Ask the user to input the first number
    number1 = float(input("Enter the first number: "))
    # Step 2: Ask the user to input the second number
    number2 = float(input("Enter the second number: "))
    # Step 3: Add the two numbers together
    sum_result = number1 + number2
    # Step 4: Display the sum to the user
    print(f"The sum of {number1} and {number2} is: {sum_result}")

calculateTheSum()