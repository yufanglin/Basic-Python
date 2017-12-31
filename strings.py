
# Create a string variable to hold the welcome message
message_double_quote = "Bobby's World"
message_single_quote = 'Bobby\'s World'

message_multi_line = '''Bobby\'s World was a good
cartoon in the 1980s'''

message_welcome = "Hello World"

print(message_multi_line)

# Find the number of characters in string
print(len(message_welcome))

# print specific characters in string
print(message_welcome[0])	# prints "H"

# print a range of characterts in string (SLICING)
print(message_welcome[0:5])  	#first number (0) is inclusive, the second (5) is not
print(message_welcome[:5])		# also prints "Hello"
print(message_welcome[6:])		# prints "World"

# all lowercase all characters
print(message_welcome.lower())

# all uppercase characters
print(message_welcome.upper())

# count number of times characters appear in our message
print(message_welcome.count('Hello'))	# Hello appears in "Hello World" once

# find the index of a character in string
print(message_welcome.find('l'))	# 'l' is first found at index 2, returns -1 if it can't find the character

# replace certain characters with another
new_msg = message_welcome.replace('World', 'Universe')	# First Arg: charcters to replace, Second Arg: what to replace with
print(new_msg)

# catenate several strings together
greeting = "Hello"
name = "my dear"

full_greeting_plus = greeting + ", " + name + ". Welcome!"
full_greeting_format = "{}, {}. Welcome!".format(greeting, name)
full_greeting_fstring = f"{greeting.upper()}, {name.upper()}. Welcome!"	# using f-strings

print(full_greeting_fstring)

# see all the functions we can use on a variable
print(dir(name))

# See more info about string methods
print(help(str))
print(help(str.lower))





