def get_last_element(lst):
    """ Prints the last element of the provided list. """
    
    # You can use either of these two methods:
    # 1. Using the index of the last element:
    print(lst[len(lst) - 1])  # This will print the last element using the length of the list
    
    # 2. Using negative indexing (this is more Pythonic):
    # print(lst[-1])  # Uncomment this line if you prefer using negative indexing
    
def main():
    # Example list to test the function
    my_list = [10, 20, 30, 40, 50]
    
    # Call the function to print the last element
    get_last_element(my_list)

# This line ensures that the main function is executed when running the script
if __name__ == '__main__':
    main()
