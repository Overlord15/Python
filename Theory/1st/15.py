basic_pay = eval(input("Enter basic pay: "))
DA = 0.97 * basic_pay  # Dearness Allowance
HRA = 0.57 * basic_pay  # House Rent Allowance
medical_allowance = 150  # Fixed medical allowance
gross_salary = basic_pay + DA + HRA + medical_allowance
EPF_deduction = 0.12 * basic_pay  # Employees' Provident Fund deduction
professional_tax = 200  # Fixed professional tax
net_salary = gross_salary - (EPF_deduction + professional_tax)
print("Net Salary:", net_salary)