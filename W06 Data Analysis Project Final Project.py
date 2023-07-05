'''An extra option added to allow the user to type in a country, while doing the analysis of
data and then displaying the minimum, maximum, and average life expectancy for that country.'''

import math

with open('life-expectancy.csv') as life_expectansies:
    next(life_expectansies)

    overall_min = 1000
    overall_max = 0
    country_highest = ''
    country_lowest = ''
    year_highest = 0
    year_lowest = 0

    users_list = []
    min_life = 1000
    max_life = 0
    min_country = ''
    max_country = ''
    total = 0

    life_list = []
    average_new = 0
    min_new = 1000
    max_new = 0

    print('Please choose from the below options on how you would like to analyze the data:')
    print('1. Entering the year of interest')
    print('2. Entering the name of the country of interest')
    choice = int(input('Please enter your chosen option here: '))
    print()

    if choice == 1:
        user_year = int(input('Enter the year of interest: '))

        for line in life_expectansies:
            clean_line = line.strip()
            parts = clean_line.split(',')

            country_name = parts[0]
            country_code = parts[1]
            year = int(parts[2])
            age_expectancy = float(parts[3])

            if age_expectancy < overall_min:
                overall_min = age_expectancy
                country_lowest = country_name
                year_lowest = year

            if age_expectancy > overall_max:
                overall_max = age_expectancy
                country_highest = country_name
                year_highest = year
        
            if user_year == year :
                users_list.append(age_expectancy)
                total = math.fsum(users_list)
                average = total / len(users_list)

                for user in users_list:
                    if user < min_life:
                        min_life = user
                        min_country = country_name

                    if user > max_life:
                        max_life = user
                        max_country = country_name

        print()
        print(f'The overall max life expectancy is: {overall_max:.3f} from {country_highest} in {year_highest}')
        print(f'The overall min life expectancy is: {overall_min:.2f} from {country_lowest} in {year_lowest}\n')

        print(f'For the year {user_year}:')
        print(f'The average life expectancy across all countries was {average:.2f}')
        print(f'The max life expectancy was in {max_country} with {max_life:.2f}')
        print(f'The min life expectancy was in {min_country} with {min_life:.3f}')

    elif choice == 2:
        country_interest = input('Please enter the name of the country of interest: ')

        for line in life_expectansies:
            clean_line = line.strip()
            parts = clean_line.split(',')

            country_name = parts[0]
            country_code = parts[1]
            year = int(parts[2])
            age_expectancy = float(parts[3])

            if age_expectancy < overall_min:
                overall_min = age_expectancy
                country_lowest = country_name
                year_lowest = year

            if age_expectancy > overall_max:
                overall_max = age_expectancy
                country_highest = country_name
                year_highest = year
        
            if country_interest.capitalize() == country_name:
                life_list.append(age_expectancy)
                total_new = math.fsum(life_list)
                average_new = total_new / len(life_list)

                for life in life_list:
                    if life < min_new:
                        min_new = life

                    if life > max_new:
                        max_new = life
        
        print()
        print(f'The overall max life expectancy is: {overall_max:.3f} from {country_highest} in {year_highest}')
        print(f'The overall min life expectancy is: {overall_min:.2f} from {country_lowest} in {year_lowest}\n')
    
        print(f'For the country {country_interest.capitalize()}:')
        print(f'the average life expectancy is {average_new:.2f}')
        print(f'The maximum life expectancy is {max_new:.2f}')
        print(f'The minimun life expectancy is {min_new:.3f}')

    else:
        print('Wrong option entered.')