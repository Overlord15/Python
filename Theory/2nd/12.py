calls = eval(input("Enter the total number of calls: "))
bill = 0
if calls <= 75:
    bill = 75
elif calls <= 150:
    bill = 75 + (calls - 75) * 0.75
elif calls <= 240:
    bill = 75 + 75 * 0.75 + (calls - 150) * 0.65
else:
    bill = 75 + 75 * 0.75 + 90 * 0.65 + (calls - 240) * 0.55
print("Monthly Bill:", bill)