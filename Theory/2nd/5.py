side1, side2, side3, side4, angle = eval(input("Enter four sides and one internal angle separated by commas: "))
if side1 == side2 == side3 == side4:
    if angle == 90:
        print("Square")
    else:
        print("Rhombus")
elif side1 == side3 and side2 == side4:
    if angle == 90:
        print("Rectangle")
    else:
        print("Parallelogram")
else:
    print("Irregular Quadrilateral")