##programmer: Andrew Fuhrmann
##the purpose of this program is to create an itemized receipt and calculate the cost of purchase

##print receipt asterisks
print("***************************************")

## Print receipt greeting
print("Andrew's Coffee and Bakedgoods\n")

##Declare input value of coffees bought
print("Number of coffees bought?")
coffee_count = int(input())

##Declare Input value of muffins bought
print("Number of muffins bought?")
muffin_count = int(input())

##print receipt asterisks and newline for whitespace
print("***************************************\n")

##Declare price for coffee_price, muffin_price. 

coffee_price = 5.00

muffin_price = 4.00

##Create equations for price for coffee_total, muffin_total, subtotal, tax, and total purcharchase amount.

coffee_total = coffee_count * coffee_price
muffin_total = muffin_count * muffin_price
subtotal = coffee_total + muffin_total
tax = (subtotal * 0.06)
total = (subtotal + tax)

print("***************************************")

##create the itemized receipt with item amounts and tax amount 
print("My Andrew's Coffee and Bakedgoods Receipt")

print(str(coffee_count) + " " + "Coffee at $5 each: $" + str(coffee_total))
print(str(muffin_count) + " " + "Muffins at $4 each: $" + str(muffin_total))
print("6% tax:", str(tax))
print("---------")
print("total: $", total)

##print receipt asterisks
print("***************************************")
