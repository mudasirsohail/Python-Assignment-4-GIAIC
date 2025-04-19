def read_phone_numbers():
    """
    Ask the user for names and numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names and numbers in the phonebook.
    """
    print("\nPhonebook Entries:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers in the phonebook
    by name.
    """
    print("\nLookup Mode:")
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{name}'s number is {phonebook[name]}")

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

# Python boilerplate to run the program
if __name__ == '__main__':
    main()
