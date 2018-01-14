student = {'name': 'John', 'age': 25, 'courses': ['English', 'CIS']}
print("Name is: " + student['name'])
print("Courses: ", student['courses'])

# using get for a nonexisting value returns none
print("Getting a nonexisting value: ",  student.get('phone'))

# for keys that don't exist, you can pass in another other argument for the method
# return instead of "none"
print("Getting a nonexisting value: ", student.get('phone', 'Not Found'))

# if a key already exist, get will return that value instead of 'Not Found'
student['phone'] = '555-5553'

print("Phone number: " + student.get('phone', 'Not Found'))

# update multiple values at a time
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5463'})
print(student)

# delete key-value
del student['age']
print("After removing age: ", student)

# remove and return the value 
phoneNum = student.pop('phone')
print("After removing phone number: ", student)
print("The phone number: " + phoneNum)

# find the number of keys in the dictionary
print("Length: ", len(student))

# return all the keys in dictionary
print("All the keys: ", student.keys())

# return all the values in dictionary
print("All the values: ", student.values())

# return all the keys and values 
print("All keys and values: ", student.items())


# loop through all keys in dictionary
for key in student:
	print("Key: " + key)

# loop through all keys/values in dictionary
for key, value in student.items():
	print("Key: ", key, " | Value: ", value)

