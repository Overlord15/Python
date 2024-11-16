n = int(input("Enter the number of rows: "))
triangle = [[1]]
for i in range(1, n):
    row = [1]
    for j in range(1, i):
        row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    row.append(1)
    triangle.append(row)
for i in range(n):
    print(' ' * (n - i - 1), end=' ')
    for j in range(i + 1):
        print(triangle[i][j], end=' ')
    print()
