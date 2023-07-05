""" few print statements added to make the program user friendly. Use of an if-elif-else statement to select the group for 
which to do calculations. A function used to eliminate repetition of codes while making the code shorter and efficient"""

print("Welcome to the Meal Price Calculator!\n")
print("Please indicate the group for which you would like to do the calculations by typing one of the numbers below?\n")
print("1. Children")
print("2. Adults")
print("3. Children and Adults\n")
group = input("Please enter the number here: ")
print(" ") # Prints blank line

def calculations_2():
    print(f"\nSubtotal: ${Subtotal:.2f}")
    sales_tax = Subtotal * (float(sales_tax_rate) / 100)
    print(f"Sales Tax: ${sales_tax:.2f}")
    meal_total_price = Subtotal + sales_tax
    print(f"Total: ${meal_total_price:.2f}\n")

    payment_amount = input("What is the payment amount? ")
    change = float(payment_amount) - meal_total_price
    print(f"Change: ${change:.2f}")

if int(group) == 1:
    childs_meal_price = input("What is the price of a child's meal? ")
    number_children = input("How many children are there? ")
    sales_tax_rate = input("What is the sales tax rate? ")
    Subtotal = int(number_children) * float(childs_meal_price)
    calculations_2()
elif int(group) == 2:
    adults_meal_price = input("What is the price of an adult's meal? ")
    number_adults = input("How many adults are there? ")
    sales_tax_rate = input("What is the sales tax rate? ")
    Subtotal = int(number_adults) * float(adults_meal_price)
    calculations_2()
elif int(group) == 3:
    childs_meal_price = input("What is the price of a child's meal? ")
    adults_meal_price = input("What is the price of an adult's meal? ")
    number_children = input("How many children are there? ")
    number_adults = input("How many adults are there? ")
    sales_tax_rate = input("What is the sales tax rate? ")

    Subtotal = (int(number_children) * float(childs_meal_price)) + (int(number_adults) * float(adults_meal_price))
    calculations_2()
else:
    pass