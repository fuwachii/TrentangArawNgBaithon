import math

# Exercise Level 1
# Day 2: 30 Days of python programming

firstName = 'Dabid'
lastName = 'Mestica'
fullName = 'Dabid Mestica'
country = 'Philippines'
city = 'Antipolo'
age = 19
year = 2026

is_married = is_true = is_light_on = False

#Exercise level 2
print(type(firstName))      # Str
print(type(lastName))       # Str
print(type(fullName))       # Str
print(type(country))        # Str
print(type(city))           # Str
print(type(age))            # Int
print(type(year))           # Int
print(type(is_married))     # Boolean
print(type(is_true))        # Boolean
print(type(is_light_on))    # Boolean

print(len(firstName))       # 5
print(len(lastName))        # 7

num_one = 5
num_two = 4

diff = num_one + num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
circum_of_circle = 2 * math.pi * radius
area_of_circle = math.pi * (radius ** 2)

print(f'The circumference and area of circle with a radius of 30 are: {circum_of_circle:.2f}, and {area_of_circle:.2f}')


radius = int(input('What is the radius of your circle?\n'))
area_of_circle = math.pi * pow(radius, 2)
print(f'The area of circle with a radius of {radius} is {area_of_circle:.2f}')

firstName = input('What is your first name?\n')
lastName = input('What is your last name?\n')
country = input('What country are you from?\n')
age = int(input('How old are you?\n'))

print(f'So you\'re {firstName} {lastName}, born and raised from {country}, and you\'re {age} years old now?')