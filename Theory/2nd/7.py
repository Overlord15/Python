year = eval(input("Enter the year: "))
months = [("January", 31), ("February", 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28),
          ("March", 31), ("April", 30), ("May", 31), ("June", 30),
          ("July", 31), ("August", 31), ("September", 30), ("October", 31),
          ("November", 30), ("December", 31)]
for month, days in months:
    print(f"{month}: {days} days")