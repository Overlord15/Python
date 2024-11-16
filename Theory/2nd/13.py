previous_reading, current_reading = eval(input("Enter previous and current meter readings separated by a comma: "))
units_consumed = (current_reading - previous_reading)
if units_consumed<0:
    units_consumed = (10**8-previous_reading)+current_reading
therms_used = int(units_consumed * 1.475)  
meter_rent = 25
if therms_used <= 125:
    rate_per_therm = 7.75
    surcharge = 0
elif therms_used <= 250:
    rate_per_therm = 9.75
    surcharge = 0.0125 * rate_per_therm
else:
    rate_per_therm = 13.00
    surcharge = 0.025 * rate_per_therm
total_cost = therms_used * (rate_per_therm + surcharge) + meter_rent
print("Gas Bill:", total_cost)