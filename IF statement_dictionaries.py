# IF statements
cars = cars = ['bmw', 'audi', 'mazda', 'subaru', 'mercedes', 'toyota', 'volkswagon']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# The if-elif-else-chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("your admission cost is $40.")
    
age = 10
if age < 4:
   price = 0
elif age < 18:
    price = 25
else:
    price = 40
    
print(f"Youe admission cost is ${price}.")

# Using multiple elif blocks
age = 70
if age < 4:
   price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    
print(f"Youe admission cost is ${price}.")

# if with lists
requested_toppings = ['mushrooms', 'olives', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    if topping == 'green peppers':
        print("sorry we are out of green peppers")
    else:
        print(f"adding {topping}.")
print("\nFinished making your pizza!")

# checking a list is not empty. If a list contains atleast 1 item, python returns a true.
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("\nFinished making your pizza")
else:
    print("are you sure you want a plain pizza?")
    
# Using Multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'extra cheese', 'pepperoni', 'pinapple']

requested_toppings = ['mushrooms', 'ham', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"sorry, {requested_topping} not available.")
        
print("\nFinished making your pizza")


# Dictionaries - key value pair
aliens = {'color': 'green', 'points': 5}
aliens['color']
aliens['points']

# Adding new key - value pairs
aliens['x_position'] = 0
aliens['y_position'] = 25
print(aliens)

# starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# modifying values in a dictionary
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position : {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien, based on its initial speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# New position = Old position + x_increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position : {alien_0['x_position']}")

# change speed to fast
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position : {alien_0['x_position']}")

# Removing Key value Pairs
aliens = {'color': 'green', 'points': 5}
print(aliens)
del aliens['points']
print(aliens)

# A dictionary of similar objects
favourite_languages = {'mike': 'sql', 'jen': 'c', 'pri': 'python', 'gerard': 'r', 'edward': 'rust', 'andy': 'java'}
language = favourite_languages['gerard'].title()
print(f"Gerard's favourite language is {language}.")

favourite_languages['mike']
favourite_languages['pri']

# using get() to access values - get() can be used to return a default value if requested key doesnt exist
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'no value assigned')
print(point_value)
# leave out the second argument and python returns none
point_value = alien_0.get('points')
print(point_value)

# looping through a dictionary
