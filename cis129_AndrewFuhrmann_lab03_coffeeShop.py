##Programmer: Andrew Fuhrmann
##The purpose of this program is to create an itemized receipt and calculate the cost of purchase

##Print receipt asterisks
print("***************************************")

##Print receipt greeting
print("Andrew's Coffee and Bakedgoods\n")

##Declare input value of coffees bought
print("Number of coffees bought?")
coffee_count = int(input())

##Declare input value of teas bought
print("Number of teas bought?")
tea_count = int(input())

##Declare input value of salads bought
print("Number of salads bought?")
salad_count = int(input())

##Declare input value of muffins bought
print("Number of muffins bought?")
muffin_count = int(input())

##Print receipt asterisks and newline for whitespace
print("***************************************\n")

##Declare price for coffee_price, muffin_price. 

coffee_price = 5.00

tea_price = 5.00

salad_price = 8.00

muffin_price = 4.00

##Create price equations for coffee_total, tea_total, salad_total, muffin_total, subtotal, tax, and total purchase amount.

coffee_total = coffee_count * coffee_price
tea_total = tea_count * tea_price
salad_total = salad_count * salad_price
muffin_total = muffin_count * muffin_price


subtotal = coffee_total + tea_total + salad_total + muffin_total
tax = (subtotal * 0.06)
total = (subtotal + tax)

print("***************************************")

##Create the itemized receipt with costs and tax amount 
print("My Andrew's Coffee and Bakedgoods Receipt")

print(str(coffee_count) + " " + "Coffees at $5 each: $" + str(coffee_total))
print(str(tea_count) + " " + "Teas at $5 each: $" + str(tea_total))
print(str(salad_count) + " " + "Salads at $8 each: $" + str(salad_total))
print(str(muffin_count) + " " + "Muffins at $4 each: $" + str(muffin_total))
print("6% tax: $", str(tax))
print("---------")
print("total: $", total)

##print thank you
print("Thank you, come again!")
##print receipt asterisks
print("***************************************")
