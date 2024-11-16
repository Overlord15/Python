# Loop through numbers from 1 to 997 (since we need three successive numbers)
for i in range(1, 20) :
    a = i
    b = i + 1
    c = i + 2
    
    # Check the condition
    if b ** 2 == a * c + 1:
        print(f"The numbers are: {a}, {b}, {c}")

# You can test this with a range smaller than 1000 for quicker results or adjust as needed.
