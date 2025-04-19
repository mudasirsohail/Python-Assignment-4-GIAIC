def get_user_numbers():
    """
    Ask the user to enter numbers one by one until a blank line is entered.
    Return the list of entered numbers.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

def count_nums(num_lst):
    """
    Count how many times each number appears in the list.
    Return a dictionary with numbers as keys and their counts as values.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    """
    Print how many times each number appears.
    """
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")

def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

# Boilerplate to call main
if __name__ == '__main__':
    main()
