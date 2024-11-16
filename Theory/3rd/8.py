x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))
total_sum = 0
sign = 1
numerator = 1
denominator = 1
for i in range(n):
    exponent = 2 * i + 1
    if i > 0:
        numerator *= (2 * i - 1)
    denominator *= (2 * i) if i > 0 else 1
    term = sign * numerator * x**exponent / denominator
    total_sum += term
    sign *= -1
print(f"The sum of the series up to {n} terms for x = {x} is: {total_sum:.2f}")
