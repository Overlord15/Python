day, month, year = eval(input("Enter day, month, and year separated by commas: "))
import datetime
try:
    date = datetime.date(year, month, day)
    print("Valid Date:", date)
except ValueError:
    print("Invalid Date")