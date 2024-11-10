import datetime

year = eval(input("Enter the year: "))

starting_day = datetime.datetime(year, 1, 1).strftime("%A")

print("The starting day of the year", year, "is:", starting_day)
