# Exercise 1
# Create a function that displays the current date.
# Hint : Use the datetime module

import datetime

def display_current_date():
    print(datetime.datetime.now().strftime("%m-%d-%Y"))


display_current_date()

# Exercise 2
# 1.Create a function that displays the amount of time left
# from now until January 1st.
# (Example: the 1st January is in 10 days and 10:34:01hours)

def time_until_january():
    x = datetime.datetime.now()
    next_year = x.year + 1
    january = datetime.datetime(next_year,1,1)
    time_until = january - x
    print(f'January 1st is in {time_until}')

time_until_january()

# Exercise 3
# Create a function that accepts a birthdate as an argument 
# (in the format of your choice), 
# and then display to the user the number of minutes he lived in his life.

def minutes_lived(year, month, date):
    x = datetime.datetime.now()
    birthdate = datetime.datetime(year,month,date)
    minutes_lived = x - birthdate
    print(f'You were born {minutes_lived} ago')

minutes_lived(1977, 7, 27)

# Exercise 4
# Write a function that display today’s date, the amount of time left 
# from now until the next holiday, additionally print what holiday that is. 
# (Example: the next holiday is in 30 days and 12:03:45 hours)
# Hint: Start with hardcoding the datetime and name of the holiday

def time_until_holiday(name_of_holiday, year, month, date):
    x = datetime.datetime.now()
    holiday = datetime.datetime(year, month, date)
    time_until = holiday - x
    print(f'{name_of_holiday} is in {time_until}')

time_until_holiday('Pesach', 2021, 3, 27)

# Exercise 5 : How Old Are You In Jupiter ?
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you were told someone were 1,000,000,000 seconds old, 
# you should be able to say that they’re 31.69 Earth-years old.

def age_in_planet_years(planet, seconds):
    planets = {
        'Mercury': .2408467,
        'Venus': .61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }
    seconds_in_earth_year = 31557600
    print(f'On planet {planet} you are: ')
    if planet == 'Earth':
        print(seconds / seconds_in_earth_year)
    elif planet == 'Mercury':
        print(seconds / (seconds_in_earth_year * planets['Mercury']))
    elif planet == 'Venus':
        print(seconds / (seconds_in_earth_year * planets['Venus']))
    elif planet == 'Mars':
        print(seconds / (seconds_in_earth_year * planets['Mars']))
    elif planet == 'Jupiter':
        print(seconds / (seconds_in_earth_year * planets['Jupiter']))
    elif planet == 'Saturn':
        print(seconds / (seconds_in_earth_year * planets['Saturn']))
    elif planet == 'Uranus':
        print(seconds / (seconds_in_earth_year * planets['Uranus']))
    elif planet == 'Neptune':
        print(seconds / (seconds_in_earth_year * planets['Neptune']))
    
seconds = 1300000000
age_in_planet_years('Earth', seconds)
age_in_planet_years('Mercury', seconds)
age_in_planet_years('Venus', seconds)
age_in_planet_years('Mars', seconds)
age_in_planet_years('Jupiter', seconds)
age_in_planet_years('Saturn', seconds)
age_in_planet_years('Uranus', seconds)
age_in_planet_years('Neptune', seconds)
