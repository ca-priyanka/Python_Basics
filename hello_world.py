print("Hello World")
print("hello Python World")
message = "Hello Python World"
print(message)
message = "hello crash course world"
print(message)
name = "priyanka bhatnagar"
print(name.title())
print(name.upper())
first_name = "priyanka"
last_name = "bhatnagar"

# Use f for formatting strings
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()} !")

# Use t for giving a tab to string
print("\tPython")

# \n is used to add a newline in a string
print("Languages:\nPython\nC\nJavaScript")

# stripping whitespace
favourite_language = 'python '
favourite_language.rstrip()

# strip whitespace from leftside of the string using lspace or bothsides using strip
favourite_language = ' python '
favourite_language.strip()

# Removing prefix or removesuffix
nonstarch_url = 'https://nonstarch.com'
nonstarch_url.removeprefix('https://')

# you can write _ in integers to make it more readable, python ignores the unerscore while printing
universe_age = 14_000_000_000
print(universe_age)

# multiple assignment - makes your code shorter
x,y,z = 1,2,3
print(x)

# constants - a variable in all capital letters is treated as constant
MAX_CONNECTIONS = 5000

# Zen of Python
import this

# LISTS
bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles[0])
print(bicycles[0].title())
message = f"My fisrt bicycle was a {bicycles[0].title()}"
print(message)

# append
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')

# insert method
motorcycles.insert(0, 'harley')

# Removing elements from list
del motorcycles[-1]
motorcycles

# using the pop() method
popped_motorcycle = motorcycles.pop()
motorcycles
print(popped_motorcycle)

# Removing item by value
motorcycles = ['harley', 'honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')

# Organising a list
# sorting a list permanently
cars = ['bmw', 'audi', 'mazda', 'subaru', 'mercedes', 'toyota', 'volkswagon']
cars.sort(reverse = True)
print(cars)

# sorting temporarily
cars = ['bmw', 'audi', 'mazda', 'subaru', 'mercedes', 'toyota', 'volkswagon']
print(f"here is the original list: {cars}")

print(f"\nhere is the sorted list:")
print(sorted(cars))

# Prtinting list in reverse order - reverses the order of the list
cars.reverse()

# Finding length of a list
len(cars)

# Looping - For loop - same action with every item in the list
# for item in list of items
for car in cars:
    print(car)
    
# Doing more within a loop
for car in cars:
    print(f"{car.title()}, is the best.")
    print(f"{car.title()}, is launcing a new model.")
    
# Doing something after a loop
magicians = ['alice', 'mike', 'david', 'timmi']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cant wait to see your next trick, {magician.title()}.\n")
print("thanks for a great show!")

# Using the Range Fuction
for value in range(1, 6):
    print(value)
    
# Using range to make a list of numbers
numbers = list(range(1,11))
print(numbers)

# even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)
# Odd numbers
odd_numbers = list(range(1,11,2))
print(odd_numbers)

# Squares
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)