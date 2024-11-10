amount = eval(input("Enter the amount of money: "))
notes_2000 = notes_500 = notes_200 = notes_100 = 0
if amount >= 2000:
    notes_2000 = amount // 2000
    amount = amount % 2000
if amount >= 500:
    notes_500 = amount // 500
    amount = amount % 500
if amount >= 200:
    notes_200 = amount // 200
    amount = amount % 200
if amount >= 100:
    notes_100 = amount // 100
    amount = amount % 100
print("2000 rupee notes:", notes_2000)
print("500 rupee notes:", notes_500)
print("200 rupee notes:", notes_200)
print("100 rupee notes:", notes_100)
