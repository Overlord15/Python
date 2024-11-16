import time

# Function to generate a random number between min and max using current time
def random_between(min_num, max_num):
    # Get the current time in seconds since the epoch and use it to create a "random" seed
    seed = int(time.time()) % (max_num - min_num + 1)
    return min_num + seed

# Input two numbers
min_num = int(input("Enter the minimum number: "))
max_num = int(input("Enter the maximum number: "))

# Ensure min_num is less than max_num
if min_num > max_num:
    min_num, max_num = max_num, min_num

# Generate and print the "random" number
print("Random number between", min_num, "and", max_num, "is:", random_between(min_num, max_num))
