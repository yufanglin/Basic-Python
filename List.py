'''
List practice in Python 3
'''

##############################      LISTS      ##############################
courses = ['History', 'Math', 'Physics', 'CompSci']

# Print the list
print(courses)
# length of the list
print(len(courses))
# Get specific values in list
print(courses[0])
# Get last value in list
print(courses[-1])
# Get the second to the last item in list
print(courses[-2])
# Get a range SLICING
print(courses[0:2])			# range includes first but not including second value
# Range: can get rid of first value if it is the first value in list, vice versa for last value
print(courses[:2])
print(courses[1:])
print(courses[:])

# Get the index of specific value
print("Index of CompSci: ", courses.index('CompSci'))

# Check if value is in the list, return true/false
print('Math' in courses)

for index, course in enumerate(courses):
	print(index, course)



###### Methods for Lists
# Add an item at the end of the lsit
courses.append('Art')
print(courses)

# Add an item at a specific position (can also insert an entire list within a list)
courses.insert(0,'CIS')
print(courses)


# add multiple values to the list
courses2 = ['Chemisty', 'Education']
courses.extend(courses2)
print(courses)

# Remove the last value of the list and return it
popped = courses.pop()
print("Popped value: ", popped)
print("Popped List: ", courses)




###### Sort list
# Reverse list
courses.reverse()
print("Reverse: ", courses)

# Sort in alphabetical order
courses.sort()
print("Alphabetical: ", courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print("Number Increase: ", nums)


# Reverse Alphabetical 
courses.sort(reverse = True)
nums.sort(reverse = True)
print("Reverse Alphabetical: ", courses)
print("Number Decrease: ", nums)

# get the sorted version of the list without altering with the original
sorted_courses = sorted(courses)
print("Sorted Courses List Version: ", sorted_courses)
print("Original Courses List: ", courses)


##### Min Max Sum
# Get min of number list
print("Number Min: ", min(nums))

# Get max of number list
print("Number Max: ", max(nums))

# Get the sum of number list
print("Sum of Number List:", sum(nums))


###### Joining strings
course_comma_str = ', '.join(courses)
courses_hyph_str = " - ".join(courses)
print("Joined Comma Courses: ", course_comma_str)
print("Joined Hyph Courses: ", courses_hyph_str)

# can make the above string back to a list
new_list = course_comma_str.split(', ')
print("Resplit String to List: ", new_list)


