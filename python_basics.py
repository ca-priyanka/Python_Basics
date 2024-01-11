# Functions
round(1.68,1)
help(round) # opens documentation
# Python has objects, objects have methods that can be called. 

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append('poolhouse')
areas.append('garage_size')


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas_sorted = areas.reverse()

# Print out areas
print(areas_sorted)

## List methods
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
downstairs = areas[:6]
upstairs = areas[6:]
print(downstairs)
print(upstairs)
## Manipulating Lists
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage" , 15.45]
print(areas_2)
# Delete list elements
# Same line command1; command2

# Separate lines
# command1
# command2
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
del(areas[-4:-2])
print(areas)
## The Python code in the script creates a list with the name areas and a copy named areas_copy. 
# Next, the first element in the areas_copy list is changed and the areas list is printed out. 
# If you hit Run Code you'll see that, although you've changed areas_copy, the change also takes effect in the areas list. 
# That's because areas and areas_copy point to the same list.
# If you want to prevent changes in areas_copy from also taking effect in areas, 
# you'll have to do a more explicit copy of the areas list. You can do this with list() or by using [:].

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
print(areas_copy)

## Functions
# function is a piece of reusable code, aimed at solving a particular task. 
# You can call functions instead of having to write code yourself.
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
int(var2)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)

##Python Packages
# to install a package http://pip.readthedocs.org/en/stable/installing/
# Download get-pip.py
# Terminal pyton3 get-pip.py
# Import the math package
import math as mt

# Definition of radius
r = 0.43

# Calculate C
C = 2*mt.pi*r

# Calculate A
A = mt.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Import radians function of math package
from math import radians

# Definition of radius
r = 192500
phi = 12
# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(phi)

# Print out dist
print(dist)

## NumPy, or Numeric Python. It's a Python package that, among others, provides a alternative to the regular python list: the NumPy array. The NumPy array is pretty similar to the list, but has one additional feature: you can perform calculations over entire arrays.
#  NumPy can do all of this so easily because it assumes that your NumPy array can only contain values of a single type. It's either an array of floats, either an array of booleans, and so on. 
# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array([baseball])

# Print out type of np_baseball
print(type(np_baseball))
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)
# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453595

# Calculate the BMI: bmi
bmi = np.array(np_weight_kg / (np_height_m**2))

# Print out bmi
print(bmi)

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = np.array(bmi < 21)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)

# Print out height of 124th player
print(np_baseball[123,0:])

