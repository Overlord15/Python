basic_pay, designation = input("Enter basic pay and designation (Manager or Officer) separated by a comma: ").split(",")
basic_pay = float(basic_pay)
designation = designation.strip()
if designation == "Manager":
    if basic_pay < 40000:
        bonus = max(0.12 * basic_pay, 2500)
    else:
        bonus = min(0.16 * basic_pay, 7500)
elif designation == "Officer" and basic_pay < 20000:
    bonus = max(0.14 * basic_pay, 2500)
    bonus = min(bonus, 5000)
else:
    bonus = 0.089 * basic_pay
print("Festival Bonus:", bonus)