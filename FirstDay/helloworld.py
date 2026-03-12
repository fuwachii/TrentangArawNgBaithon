import math
a = 3
b = 4

#Exercise Level 1
#Exercise 1.1
print('Hello World!')
print('My Python version is 3.13.12! I used python --version to look for the version of my Python!')

# Exercise 1.2
print(a + b)    # Addition (+)
print(a - b)    # Subtraction (-)
print(a * b)    # Multiplication (*)
print(a % b)    # Modulus (%)
print(a / b)    # Division (/)
print(a ** b)   # Exponential (**)
print(a // b)   # Floor Division (//)

#Exercise 1.3
print('David')
print('Mestica')
print('Philippines')
print('I am enjoying 30 days of python')

#Exercise 1.4
print(type(10))     # Int
print(type(9.8))    # Float
print(type(3.14))   # Float
print(type(4 - 4j))     # Complex
print(type(['Asabeneh', 'Python', 'Finland']))  # List
print(type('David'))    # String
print(type('Mestica'))  # String
print(type('Philippines'))  # String

#Exercise Level 2
print('Done creating a folder and the helloworld.py file! If you can see this, it means it runs!')  # String

#Exercise Level 3
print(type(15))     # Int
print(type(1.5))    # Float
print(type(1 + 4j))     # Complex
print(type('String'))   # String
print(type(True))   # Boolean
print(type(False))  # Boolean
print(type(['Jeanne', 'Shiro', 'Astolfo'])) # List
print(type(('Addition', 'Subtraction', 'Multiplication', 'Division')))  # Tuple
print(type({'Wife':'Astolfo'})) # Dictionary
print(type({1, 2, 3}))  # Set

def euclidean_distance(p1, p2):
    sum_sq = sum([(coord1 - coord2) ** 2 for coord1, coord2 in zip(p1, p2)])
    return math.sqrt(sum_sq)

point1 = (2, 3)
point2 = (10, 8)

distance = euclidean_distance(point1, point2)

print(f'The euclidean distance is: {distance}')