def main():
    lst = []  # Create an empty list to store the values
    
    # Start asking the user for input
    val = input("Enter a value: ")  # Get the first input
    while val:  # If the user enters something (input is not empty)
        lst.append(val)  # Add the entered value to the list
        val = input("Enter a value: ")  # Ask for the next input
    
    # Print the final list after the user presses enter without typing anything
    print("Here's the list:", lst)

# This provided line ensures that the main function runs when executing the script
if __name__ == '__main__':
    main()
