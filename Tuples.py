'''
Tuple practice in Python 3
'''

####### Tuples cannot be modified. Immutable

####  Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

# since list 2 & list 1 are the same mutable, once list 1 is changed, so is list2
print(list_1)
print(list_2)

#### Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'	# type error
print(tuple_1)
print(tuple_2)