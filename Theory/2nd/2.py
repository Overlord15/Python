num1, num2 = eval(input("Enter two numbers separated by a comma: "))
if num1 > num2:
    print("Greater number:", num1)
elif num2 > num1:
    print("Greater number:", num2)
else:
    print("Both numbers are equal.")