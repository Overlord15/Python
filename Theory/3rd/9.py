counter = 0

for num in range(2, 10000):
    # Check if num is prime
    is_prime = True
    if num < 2:
        is_prime = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    # Check if num + 2 is prime
    is_twin_prime = True
    twin_num = num + 2
    for i in range(2, int(twin_num ** 0.5) + 1):
        if twin_num % i == 0:
            is_twin_prime = False
            break

    # If both num and num + 2 are prime, print the pair and increment the counter
    if is_prime and is_twin_prime:
        counter += 1
        print(f"{counter}: {num}, {twin_num}")
