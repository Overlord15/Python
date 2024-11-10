pound_to_inr = 101.58 
dollar_to_inr = 74.32 
euro_to_inr = 87.67   
amount = eval(input("Enter the amount in Pounds, Dollar, and Euro separated by commas: "))
pounds, dollars, euros = amount
print("INR equivalent of Pounds:", pounds * pound_to_inr)
print("INR equivalent of Dollars:", dollars * dollar_to_inr)
print("INR equivalent of Euros:", euros * euro_to_inr)