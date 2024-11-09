def present_value_of_payments(p, r, e):
    r_decimal = r / 100  # Convert percentage to decimal
    total_payment = 0
    for i in range(e):
        total_payment += p / ((1 + r_decimal) ** i)
    return total_payment

p, r, e = input("Enter yearly payment, inflation rate and expectancy separated by space: ").split()
p = eval(p)
r = eval(r)
e = eval(e)

total_payment = present_value_of_payments(p, r, e)
print(f"The present value of total payments is: {total_payment:.2f}")
