'''An else statement added to the menu with a guiding message incase of an incorect action
storing. Code added to allow usuer to enter quantity of items'''
import math

items_list = []
prices = []
items_quantities = []

action = 0

print('Welcome to the Shopping Cart Program!\n')

while action != 5:
    multiplications = []
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')

    action = int(input('Please enter an action: '))

    if action == 1:
        item_added = input('What item would you like to add? ')
        price_added = float(input(f'What is the price of {item_added}? '))
        quantity_added = int(input(f'Please enter the the quantity of {item_added} you would like to purchase. '))

        items_list.append(item_added)
        prices.append(price_added)
        items_quantities.append(quantity_added)

        print(f'{item_added} has been added to the cart.')
        print()
    elif action == 2:
        if items_list:
            print('The contents of the shopping cart are:')

            for i in range(len(items_list)):
                item = items_list[i]
                price = prices[i]
                quantity = items_quantities[i]

                print(f"{i+1}. {item} - ${price:.2f} - Qty:{quantity}")
        else :
            print('There are no items in in your in your shopping cart.')
        print()
    elif action == 3:
        if items_list:
            removed_item = int(input('Which item would you like to remove? '))
            index = removed_item -1

            if index in range(0, len(prices)):
                items_list.pop(index)
                prices.pop(index)
                items_quantities.pop(index)
                print('Item removed.')
            else:
                print('Sorry, that is not a valid item number.')
        else:
            print('There are no items in in your in your shopping cart.')
    elif action == 4:
        if items_list:
            for i in range(len(prices)):
                price = prices[i]
                quantity = items_quantities[i]
                multiplication = (price * quantity)
                multiplications.append(multiplication)
            total_price = math.fsum(multiplications)

            print(f'The total price of the items in the shopping cart is ${total_price:.2f}')
        else:
            print('There are no items in in your in your shopping cart.')
        print()
    else:
        print('Please choose a correct action.')

print('Thank you. Goodbye.')