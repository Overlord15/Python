length, width, height, cost_per_unit_area = eval(input("Enter length, width, height of room, and cost per square unit separated by commas: "))
wall_area = 2 * height * (length + width)
painting_cost = wall_area * cost_per_unit_area
print("Area of Walls:", wall_area)
print("Cost of Painting:", painting_cost)