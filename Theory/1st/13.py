length = eval(input("Enter the effective length of the pendulum in meters: "))
import math
gravity = (4 * math.pi ** 2 * length) / (1 ** 2)  # assuming time period of 1 second for simplicity
print("Acceleration due to Gravity:", gravity)