def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Keep doubling the value until it's 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# Required to run the main function
if __name__ == '__main__':
    main()
