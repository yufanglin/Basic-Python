'''
    Code taken while following these Python tutorials:
    https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''
nums = [1, 2, 3, 4, 5]

print("Looping through number array: ")
for num in nums:
	if num == 2:
		print("Found 2!")
		continue
	elif num == 4:
		print("Found 4! Breaking...")
		break

	print(num)

print("---------------------------------\n")
print("Loop within a loop: ")

for num in nums:
	for letter in 'abc':
		print(num, letter)

print("---------------------------------\n")
print("Go through a loop n amount of times: ")
for i in range(1, 11):
	print(i)

print("---------------------------------\n")
print("While Loops - loop n amount of times: ")

x = 0
while x < 10:
	if x == 8:
		print(x, ", breaking....")
		break
	print(x)
	x += 1

print("---------------------------------\n")
print("While Loops - Infinite loop: ")

y = 0
while True:
	if y == 6:
	 	print(y, ", breaking...")
		break
	print(y)
	y += 1

print("---------------------------------\n")
