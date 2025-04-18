def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    numbers: list[int] = [5,4,3,2,1]  # List of numbers to sum
    sum_of_numbers: int = add_many_numbers(numbers)  # Call the function to sum the list
    print(sum_of_numbers)  # Output the sum of the numbers

if __name__ == '__main__':
    main()
