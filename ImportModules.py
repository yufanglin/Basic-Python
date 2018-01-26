'''
Code from following: https://www.youtube.com/watch?v=CqvZ3vGoGs0&index=9&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''

# import my_module as mm
# from my_module import *	// imports everything
import sys
# directly add a path program will look for modules
# sys.path.append("Users/.....")
# Or add the enviroment variable by:
# go to terminal:	$ nano ~/.bash_profile
# In profile, add: export PYTHONPATH="/Users/...."

import random
import math
import datetime
import calendar
import os  					# access to underlying operating system

from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print("Index for math: 				", index)
print("Test variable from module: 	", test)

print("\n-------------------------------\n")
# the path that program looks for the imported modules
print("Sys path: ", sys.path)

print("\n---------------Random Library----------------\n")
# pick a random course in our course array
random_course = random.choice(courses)
print("Random Course:				", random_course)


print("\n---------------Math Library----------------\n")
# convert integer to radians
rads = math.radians(90)
print("Radians for 90:				", rads)
print("Sin of the radian 90:		", math.sin(rads))
print("Cos of the radian 90:		", math.cos(rads))


print("\n---------------Datetime Library----------------\n")
# Get today's date
today = datetime.date.today()
print("Today is:					", today)


print("\n---------------Calendar Library----------------\n")
# Check if 2017 is a leap year
print("2017 is a leap year:			", calendar.isleap(2017))
print("2020 is a leap year:			", calendar.isleap(2020))


print("\n---------------OS Library----------------\n")
# get the current working directory
print("Current working directory:	", os.getcwd())
print("os library file location:	", os.__file__)






