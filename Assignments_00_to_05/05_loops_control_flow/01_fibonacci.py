MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")
        # Update terms
        curr_term, next_term = next_term, curr_term + next_term

# This line ensures main() runs when script is executed
if __name__ == '__main__':
    main()
