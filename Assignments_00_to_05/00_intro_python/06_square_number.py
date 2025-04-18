def main():
    # Ask the user for a number and convert it to float
    num: float = float(input("Type a number to see its square: "))

    # Calculate and print the square of the number
    square: float = num ** 2
    print(str(num) + " squared is " + str(square))


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
