# import time


# def countdownTimer(t):
#     while t:
#         mins, secs = divmod(t , 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end='\r')
#         time.sleep(1)
#         t -= 1

#     print("Timer Completed!!")

# t = input("Enter a time in Seconds?  ")
# countdownTimer(int(t)) 



import time

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)  # Convert total time into minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Format time as mm:ss
        print(timer, end='\r')  # Print the timer on the same line
        time.sleep(1)  # Wait for one second
        t -= 1  # Decrement the time

    print("Timer Completed!!")

def get_input():
    while True:
        try:
            t = int(input("Enter time in seconds: "))
            if t <= 0:
                print("Please enter a positive number.")
            else:
                return t
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Get user input and start countdown
time_in_seconds = get_input()
countdown_timer(time_in_seconds)
