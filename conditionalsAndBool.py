
'''
From Corey Schafer's tutorials on youtube
'''

print("\n")
if True:
	# will print this statement unless True was changed to False
	print('Conditional was True')

# Comparisons:
# Equal: 			==
# Not Equal:		!=
# Greater than: 	>
# Less Than:		<
# Greater or Equal:	>=
# Less or Equal: 	<=
# Object Identity:	is


print("\n---------------------------\n")

language = 'C++'

if language == 'Python':
	print('Language is Python.')

elif language == 'C++':
	print('Language is C++.')

elif language == 'Java':
	print('Language is Java')

elif language == 'C#':
	print('Language is C#')

elif language == 'C':
	print('Language is "C')

else:
	print('No language match.')


print("\n---------------------------\n")

# and
# or 
# not

user = 'User'
logged_in = True

if user == 'Admin' and logged_in:
	print("Admin Page")

elif not logged_in:
	print("Please Log In")

elif user != 'Admin' and logged_in:
	print("Regular User")

elif user == 'Admin' or logged_in:
	print("Either logged in or Admin")

else:
	print("Bad Creds")

print("\n---------------------------\n")

# compare if two objects are equal in memory
a = [1, 2, 3]
b = [1, 2, 3]

print("Do the values of a and b equal?: ", a == b)
print("are the objects a and b the same in memory?: ", a is b)

print("ID of 'a' in memory: ", id(a))
print("ID of 'b' in memory: ", id(b))

c = b
print("\nAre objects c and b the same in memory?: ", c is b)
print("ID of 'c' in memory: ", id(c))

print("\n---------------------------\n")

# What Python evaluates as False values:
	# False
	# None
	# Zero of any numeric type
	# Any empty sequence. For example, '', (), []
	# Any empty mapping. For example, {}.

condition = ["items"]
if condition:
	print('Evaluated to True, condition was: ', condition)
else:
	print('Evaluated to False, condition was: ', condition)

print("\n---------------------------\n")
