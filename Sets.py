'''
Set practice in Python 3
'''

# Sets or unordered and have no duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print("Original Courses: ", cs_courses)
print('Math' in cs_courses)

# try to have a duplicate
dupli_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print("Duplicate Courses: ", dupli_courses)

art_courses = {'History', 'Math', 'Art', 'Design'}

# see what these courses have in common
print("Same Courses", cs_courses.intersection(art_courses))

# combine courses
print("Combine courses: ", cs_courses.union(art_courses))

# Empty Set
empty_set = set()
