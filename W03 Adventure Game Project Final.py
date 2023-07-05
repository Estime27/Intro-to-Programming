"""Nested functions,Lists and while loops used to create an 
efficient program and handle incorect inputs until correct option is entered."""

def tourist_choice():
    choice = ['ask', 'ignore','ASK','IGNORE','Ask','Ignore']
    print('\nUp ahead you see someone wearing a cap that looks like one of your group members.')
    print('As you get closer to the person, you realise that he is not one of your group')
    print('members. Do you stop and ASK him for directions or IGNORE him?')
    user_input = ''
    while user_input.lower() not in choice:
        print('Availabele options: ASK/IGNORE')
        user_input = input()
        if user_input.lower() == 'ask':
            print('\nWin: The person gives you the right directions and you find your group members.')
        elif user_input.lower() == 'ignore':
            print('\nGame Over: As you continue walking you realise that the road comes to an end.')
        else:
            print('\nPlease enter the correct option')

def junction_3():
    directions = ['forward','backwards','left','FORWARD','BACKWARDS','LEFT','Forward','Backwards','Left']
    print('\nAs you continue walking you arrive at another T-Junction.')
    print('Up ahead in the road, you see something moving like a bear!')
    print('Where do you go?')
    user_input = ''
    while user_input not in directions:
        print('Available options: FORWARD/BACKWARDS/LEFT')
        user_input = input()
        if user_input.lower() == 'forward':
            print('\nWin: As you get closer you see that it was just a drunk man')
            print('and right after the drunk man you see the tour guide and your group')
        elif user_input.lower() == 'backwards':
            print('\nGame Over: You are lost')
        elif user_input.lower() == 'left':
            print('\nWin: In the road there is a public phone that you can use to')
            print('call the tour guide or one of your group members.')
        else:
            print('\nPlease enter the correct option')

def junction_2(): 
    directions = ['left','right','LEFT','RIGHT','Left','Right']
    print('\nAs you keep on walking you arrive at another T-junction with two roads in front of you.')
    print('The left road is bushy and the road on the right is clear.')
    print('Where would you like to go?')
    user_input = ''
    while user_input not in directions:
        print('Available road options: LEFT/RIGHT')
        user_input = input()
        if user_input.lower() == 'left':
            print('\nGame Over: Bitten by a snake')
        elif user_input.lower() == 'right':
            tourist_choice()
        else:
            print('\nPlease enter the correct option')

def main_junction():
    directions = ['left','right','LEFT','RIGHT','Left', 'Right']
    print('You find yourself at a T-junction. Where do you go?')
    user_input = '' #initializing empty space to the variable so that when compared in the while loop to the variable
    #directions the while loop evaluates to true because empty space is not in the directions variable.
    while user_input not in directions: #initially the while loop will always evaluate to true.
        print('Available road options: LEFT/RIGHT ')
        user_input = input() #Now it asks for the input from the user LEFT/RIGHT
        if user_input.lower() == 'left': #If "left" it loops back to the top and compares left with the values in directions
            junction_2()                 #variable. the while loop evaluates false, exits the loop while calling junction_2().
        elif user_input.lower() == 'right':
            junction_3()
        else: #If an incorect value is entered, loops to the top of the while and that values gets compared to the value 
            print('\nPlease enter the correct option.') # in direction variable and execute the prompt question again

name = input('Please enter your first name: ')
print(f'\nWelcome to the Adventure Game {name.capitalize()}!\n')
print('You are a tourist in Cape Town with your group and a tour guide.')
print('However, you fall behind and you lose sight of your group and the')
print("tour guide during the group's visit of roben island.")
print('After walking a little while trying to catch up to your group, you')
main_junction()