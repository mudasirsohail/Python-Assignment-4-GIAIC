def main():
    # Prompt the user to enter the lengths of the three sides
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter: float = side1 + side2 + side3

    # Print the result
    print("The perimeter of the triangle is " + str(perimeter))

# Required line to call main() function
if __name__ == '__main__':
    main()
