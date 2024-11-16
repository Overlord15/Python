start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for num in range(start, end + 1):
    s = 0
    f = 0
    s1 = 0
    s2 = 0
    for i in range(1, num + 1):
        if num % i == 0:
            s += i
            f += 1
    for j in range(1, s):
        if s % j == 0:
            s1 += j
    for j in range(1, f):
        if f % j == 0:
            s2 += j
    if s1 == s and s2 == f:
        print(num, "is a sublime number")
