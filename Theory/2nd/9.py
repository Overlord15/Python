angle1, angle2, angle3 = eval(input("Enter the three angles of the triangle separated by commas: "))
if angle1 + angle2 + angle3 != 180:
    print("Invalid triangle")
elif angle1 == angle2 == angle3 == 60:
    print("Equiangular triangle")
elif 90 in [angle1, angle2, angle3]:
    print("Right-angle triangle")
elif all(angle < 90 for angle in [angle1, angle2, angle3]):
    print("Acute-angled triangle")
else:
    print("Obtuse-angled triangle")