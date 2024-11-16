start_range = eval(input("Enter start range:"))
end_range = eval(input("Enter end range:"))
print("Pandigital numbers in given range:")
for num in range(start_range, end_range + 1):
    num_str = str(num)
    digits = "0123456789"
    is_pandigital = True
    for digit in digits:
        if digit not in num_str:
            is_pandigital = False
            break
    if is_pandigital:
        print(num, "is a Pandigital number")