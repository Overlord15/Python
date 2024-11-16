x = 1
while x <= 100:
    y = x 
    while y <= 100:
        z = y
        while z <= 100:
            if z * z == x * x + y * y:
                print(x, y, z)
            z = z + 1
        y = y + 1
    x = x + 1
