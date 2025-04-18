"""
Program: add2numbers
--------------------
This program asks the user for two
integers and prints their sum.
"""

def main():
    print("This program adds two numbers.")
    
    # Prompt and convert inputs to integers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Calculate the sum
    total = num1 + num2
    
    # Display the result
    print("The total is " + str(total) + ".")

# Required to call the main function
if __name__ == '__main__':
    main()
