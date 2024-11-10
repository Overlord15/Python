cost_price, selling_price = eval(input("Enter cost price and selling price separated by a comma: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss:", loss)
else:
    print("No profit, no loss.")