total_hours = float(input("Enter the total number of hours the car was parked: "))
charge = 0
if total_hours <= 8.5:
    charge = 55
else:
    charge = 55
    remaining_hours = total_hours - 8.5
    additional_blocks = (remaining_hours + 1.99) // 2  
    charge += additional_blocks * 13.75
    if total_hours > 23:
        extra_time_in_minutes = (total_hours - 23) * 60
        charge += extra_time_in_minutes * 5.50
print("The total parking charge is Rs.", charge)
