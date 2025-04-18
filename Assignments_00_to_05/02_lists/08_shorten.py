MAX_LENGTH = 3  # Maximum length for the list

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Keep removing elements if the list is longer than MAX_LENGTH
        last_elem = lst.pop()  # Remove and return the last element of the list
        print(last_elem)  # Print the element that is removed

# This function is used to collect a list from the user
def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Keep asking for input until the user presses Enter without entering anything
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    shorten(lst)  # Call shorten to reduce the list size to MAX_LENGTH

if __name__ == '__main__':
    main()
