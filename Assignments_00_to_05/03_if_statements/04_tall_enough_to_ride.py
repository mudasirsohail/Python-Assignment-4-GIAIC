MINIMUM_HEIGHT: int = 5.0

def main():
    while True:
        user_input = input("How tall are you? (Press Enter to quit) ")
        
        # Exit condition
        if user_input == "":
            print("Goodbye!")
            break

        # Try to convert input to float
        try:
            height = float(user_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()
