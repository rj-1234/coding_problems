"""
3. Two Sum III – Data structure design

Question:
Design and implement a TwoSum class. It should support the following operations: add
and find.
add(input) – Add the number input to an internal data structure.
find(value) – Find if there exists any pair of numbers which sum is equal to the value.
For example,
add(1); add(3); add(5); find(4)  true; find(7)  false
"""

class TwoSum:
	"""docstring for ClassName"""
	def __init__(self):
		self.table = dict()

	def add(self, number):
		if number in self.table:
			self.table[number] += 1
		else:
			self.table[number] = 1

	def find(self, value):
		for key in self.table:
			if value == key * 2:
				if self.table[key] > = 2:
					return true

			else:
				if value - key in self.table:
					return True

		return False