'''
Sorting Lists, Tuples, and Objects
Code from following this tutorial: 
https://www.youtube.com/watch?v=D3JvDWO-BY4&index=21&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''

# sort
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)
desc_li = sorted(li, reverse=True)

print('Sorted Variable:\t', s_li)
print('Descending Sorted:\t', desc_li)
print('Original Variable:\t', li)

# sort original
li.sort()
print('\nSorted Orignal:\t', li)
li.sort(reverse=True)
print('Descending Sorted:\t', li)



tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print('\nTuple\t', s_tup)
print('Original Variable:\t', tup)

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('\nDict\t', s_di)
print('Original Variable:\t', di)


li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print("\nSorted:\t", s_li)
print("Original:\t", li)

class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return '({}, {}, ${})'.format(self.name, self.age, self.salary)

	def e_sort(emp):
		return emp.name

from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]
print('\nOriginal Employees List:\t', employees)
s_employees = sorted(employees, key=Employee.e_sort, reverse=True)
#Lambda version:
# s_employees = sorted(employees, key=lambda e: e.name, reverse=True)

# operator.attrgetter Version:
# s_employees = sorted(employees, key=attrgetter('age'))

print('\nReverse Sorted:\t', s_employees)

