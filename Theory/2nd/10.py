side1, side2, side3 = eval(input("Enter the three sides of the triangle separated by commas: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid triangle sides")