# create an integer variable
num_int = 3
print(type(num_int))

# create a float variable
num_float = 3.14
print(type(num_float))

# Arithmetic Operations:
add = 3 + 2			# should return 5
sub = 3 - 2			# should return 1
mult = 3 * 2		# should return 6
div = 3 / 2			# should return 1.5
floor_div = 3 // 2	# should return 1
expo = 3 ** 2		# should return 9
mod = 3 % 2			# should return 1

print(add)
print(sub)
print(mult)
print(div)
print(floor_div)
print(expo)
print(mod)

num = 1
num *= 10 
print(num)		# should return 10

# absolute numbers
print(abs(-3))		# should return 3

# round the numbers
print(round(3.75))	# should return 4
print(round(3.25))	# should return 3
print(round(3.25, 1))	# round to nearest tenth (which is 3.2)




## Comparison Operations:
print(3 == 2)
print (3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)


num_1 = '100'
num_2 = '200'

print(num_1 + num_2)		# return 100200 because the variables are strings

# cast string to integer
num_3 = int(num_1)
num_4 = int(num_2)
print(num_3 + num_4)		# should return 300

