'''
LEGB
Local, Enclosing, Global, Built-in
Code from following this tutorial: 
https://www.youtube.com/watch?v=QVdf0LgmICw&index=18&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''

import builtins

# print out all the builtin modules
#print(dir(builtins))

# def min():
# 	pass

def my_min():
	pass


x = 'global x'
v = 'global v'

# Enclosing
def outer():
	x = 'outer x'
	# if comment local x, will look for global x

	# nested function
	def inner():
		# nonlocal x
		# if uncomment "nonlocal x", the outer x will be changed to inner x
		x = 'inner x'
		#if comment enclosing x, then python checks for local x
		print(x)

	inner()
	print(x)

outer()

# Built-in Scope
m = min([5, 1, 4, 2, 3])	# if min() not commented out, will have error, because python found custom min before builtin
print(m)

def test(z):
	global x
	x = 'reseting global x'
	y = 'local y'
	v = 'local v'
	print(y + " in test function")
	print(v + " in test function")
	print(x + " in test function")
	print(z + " in test function")

test('local z')
#print(y) <-- this will cause an error
print(x + " outside functions")