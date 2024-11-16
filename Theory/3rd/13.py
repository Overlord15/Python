date_input = input("Enter the date (e.g., 19/7/2019 or 19th July, 2019): ")
long_hand_suffixes = ["st", "nd", "rd", "th"]
long_hand_months = ["january", "february", "march", "april", "may", "june",
                    "july", "august", "september", "october", "november", "december"]
for suffix in long_hand_suffixes:
    date_input = date_input.replace(suffix, "")
date_input = date_input.replace(",", "")
parsed_date = None
parts = date_input.split()
if len(parts) == 3:
    day = int(parts[0])
    month_str = parts[1].lower()
    year = int(parts[2])
    if month_str in long_hand_months:
        month = long_hand_months.index(month_str) + 1
        parsed_date = (day, month, year)
else:
    parts = date_input.split('/')
    if len(parts) == 3:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
        parsed_date = (day, month, year)
if parsed_date:
    day, month, year = parsed_date
    valid_date = True
    if month < 1 or month > 12:
        valid_date = False
    if day < 1:
        valid_date = False
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        valid_date = False
    if month in [4, 6, 9, 11] and day > 30:
        valid_date = False
    if month == 2:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and day > 29:
            valid_date = False
        if (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)) and day > 28:
            valid_date = False
    if valid_date:
        print("The date is valid.")
    else:
        print("The date is not valid.")
else:
    print("The date format is not recognized.")
