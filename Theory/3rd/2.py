p = int(input("Enter value of p: "))
q = int(input("Enter value of q: "))
limit = int(input("Enter value of upper limit: "))
i = 1
print("Whle numbers which are divided by p and not by q in the given range are:")
while i <= limit:
    if i % p == 0 and i % q != 0:
        print(i)
    i = i + 1
