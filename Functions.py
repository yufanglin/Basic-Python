'''
    Code taken while following these Python tutorials:
    https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''

print("Functions are a great way to keep your code DRY: 'Don't Repeat Yourself'\n\n")
print("----------------------------------\n")
print("Intro to Functions:\n")

def hello_func():
	return "Hello Function!"

print("Printing a function w/o '()': ", hello_func)
print("Printing a function w/ '()': ", hello_func())
print("Print function with uppercase: ", hello_func().upper())

print("----------------------------------\n")
print("Function with an argument\n")

def hello_func_greet(greeting):
	return "{} function!".format(greeting)

print("Pass 'Goodnight' to funciton: ", hello_func_greet("Goodnight"))
print("----------------------------------\n")
print("Function with default argument value\n")

def hello_func_default_greet(greeting, name = " You"):
	return "{}, {}".format(greeting, name)


print("Call function using a default value: ", hello_func_default_greet("Goodnight"))
print("Call function without default value: ", hello_func_default_greet("Goodnight", "my love."))

print("----------------------------------\n")
print("Accept an arbitrary number of positional or keyboard arguments: \n")

def student_info(*args, **kwargs):
	studentName = ''
	studentAge = 0

	# Get student names
	if 'name' in kwargs:
		studentName = kwargs['name']

	# Get the age
	if 'age' in kwargs:
		studentAge = kwargs['age']

	return "{}, age {}, is taking: {}".format(studentName, studentAge, args)

print(student_info('English', 'Art', name='Mimi', age=17))
print(student_info('Math', 'Biology', name='Sara', age=18))

courses = ['History', 'Economy', 'Math']
info = {'name': 'Junpei', 'age': '14'}
print("Passing arguments with *: ", student_info(*courses, **info))

print("----------------------------------\n")
print(" Final: Leap Year Functions \n")


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	'''
	Return True for leap years, False for non-leap years.
	'''
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
	'''
	Return number of days in that month in that year.
	'''

	# check if the month is valid
	if not 1<= month <= 12:
		return 'Invalid Month'

	# Check if it's a leap year february 
	if month == 2 and is_leap(year):
		return 29

	# otherwise, return the number of days from the array
	return month_days[month]

print("Is 2017 a leap year?: ", is_leap(2017))
print("Is 2020 a leap year?: ", is_leap(2020))

print("What is the number of days in February of 2017: ", days_in_month(2017, 2))
print("What is the number of days in February of 2020: ", days_in_month(2020, 2))

print("----------------------------------\n")
