'''
Comprehensions
Code from following this tutorial: 
https://www.youtube.com/watch?v=3dt4OGnU5sM&index=20&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# want 'n' for each 'n' in nums
my_list = []
for n in nums:
	my_list.append(n)
print("list if n of nums: ", my_list)

# list comprehension of above
my_list = [n for n in nums]
print("list comprehension: ", my_list)



# I want 'n * n' for each 'n' in nums
my_list = []
for n in nums:
	my_list.append(n*n)
print("\nlist of n * n: ", my_list)

# list comprehension of above
my_list = [n*n for n in nums]
print("list comprehension: ", my_list)

# using a map + lambda
my_list = map(lambda n: n*n, nums)
print("Map + lambda for n * n: ", my_list)



# I want n for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
	if(n%2 == 0):
		my_list.append(n)
print("\nEven list: ", my_list)

# List comprehension of above
my_list = [n for n in nums if n%2 == 0]
print("list comprehension: ", my_list)

# using filter + lambda
my_list = filter(lambda n: n%2 == 0, nums)
print("Filter + lambda: ", my_list)



# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
	for num in range(4):
		my_list.append((letter, num))
print("\n(letter, num) pair: ", my_list)

# list comprehension of above
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print("list comprehension: ", my_list)


# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print("\nZip names + heroes list: ", zip(names, heroes))

# I want a dict{'name': 'hero'} for each name, hero in zip(names, heroes)
my_dict = {}
for name, hero in zip(names, heroes):
	my_dict[name] = hero
print("Regular dictionary: ", my_dict)

# list comprehension
my_dict = {name: hero for name, hero in zip(names, heroes)}
print("list Comprehension: ", my_dict)

# if name not equal to Peter
my_dict = {name: hero for name, hero in zip(names,heroes) if name != 'Peter'}
print("list comprehension without Peter: ", my_dict)



# Set Comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
	my_set.add(n)
print("\nSet: ", my_set)

# list comprehension
my_set = {n for n in nums}
print('list comprehension: ', my_set)


# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
def gen_func(nums):
	for n in nums:
		yield n*n
my_gen = gen_func(nums)

print("\nGenerator Expressions: ")
for i in my_gen:
	print(i)

# list comprehension
my_gen = (n*n for n in nums)
print("list comprehension: ", my_gen)
