# Conversion constant for feet to inches
INCHES_IN_FOOT: int = 12  # There are 12 inches in 1 foot

def main():
    # Get user input for the number of feet
    feet: float = float(input("Enter number of feet: "))
    
    # Perform the conversion from feet to inches
    inches: float = feet * INCHES_IN_FOOT
    
    # Display the result
    print(f"That is {inches} inches!")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
