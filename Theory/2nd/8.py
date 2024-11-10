
sales_a, sales_b = eval(input("Enter sales in region A and region B separated by a comma: "))

if sales_a < 10000:
    commission = 0
    print("Commission: Nil (No commission)")

elif sales_b < 15000 and sales_a < 16000:
    commission = 0.065 * (sales_a + sales_b)
    print("Commission:", commission)

elif 15000 <= sales_b < 25000 and 16000 <= sales_a < 35000:
    commission = 0.085 * (sales_a + sales_b) + 1500
    print("Commission:", commission)

else:
    commission = 0.11 * (sales_a + sales_b) + 4500
    print("Commission:", commission)
