""" Addition: An Extra clever story added to the core requirrements.
 A conditional if-else statement used to provide access to the additional clever story.
"""
print('Please enter the following:\n')
adj = input('adjective: ')
anml = input('animal: ')
verb_0 = input('verb: ')
exclmtion = input('exclamation: ')
verb_1 = input('verb: ')
verb_2 = input('verb: ')

output = f'{adj.lower()} {anml.lower()} {verb_0.lower()} down the hallway. "{exclmtion.capitalize()}!" I yelled. But all'
output_0 = f'I could think to do was to {verb_1.lower()} over and over. Miraculously,'
output_1 = f'that caused it to stop, but not before it tried to {verb_2.lower()}'

print('\nYour story is: \n')
print('The other day, I was really in trouble. It all started when I saw a very')
print(output)
print(output_0)
print(output_1)
print('right in front of my family.')

x = input('\nWould you like to try another clever story?')
if x=='yes' or x=='YES':
    print('\nPlease enter the following:\n')
    adjactive = input('adjective : ')
    color = input('color name : ')
    thing = input('thing name :')
    place = input('place name : ')
    person= input('person name : ')
    adjactive1 = input('adjective : ')
    insect= input('insect name : ')
    food = input('food name : ')
    verb = input('verb name : ')
    output_2 = f'Last night I dreamed I was a {adjactive.lower()} butterfly with {color.lower()} splocthes'
    output_3 = f'that looked like {thing.lower()}. I flew to {place.title()} with my bestfriend and'
    output_4 = f'{person.capitalize()} who was a {insect.lower()}. We ate some {food.lower()} when we got there'
    output_5 = f'and then decided to {verb.lower()} and the dream ended when I said-- lets {verb.lower()}.'
    print('\nYour story is: \n')
    print(output_2)
    print(output_3)
    print(output_4)
    print(output_5)

else:
    pass 