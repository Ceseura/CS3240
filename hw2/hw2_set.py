
class OurSet():
	""" A Class which represents a set. Items can be added, union and intersection operations are implemented, as well as __str__() __len__() and __iter__(). """
	def __init__(self):
		""" Create a new 'OurSet' object. """
		self.data = [];

	def add(self, item):
		""" If 'item' is not already in the set, add 'item' to the set. Return true if 'item' was added, otherwise return false. """
		if item not in self:
			self.data.append(item)
			return True
		return False

	def add_list(self, list):
		""" For each item in 'list', if the item is not already in the set, add it to the set. Return true if any item was added, otherwise return false. """
		returnMe = False
		for item in list:
			if item not in self:
				self.data.append(item)
				returnMe = True

		return returnMe

	def __str__(self):
		""" Return the string representation of the set. """
		return "<{}>".format(self.data.__str__()[1:-1])

	def __len__(self):
		""" Return the number of items in the set. """
		return len(self.data);

	def __iter__(self):
		""" Return an iterator over all of the items in the set. """
		return self.data.__iter__()

	def union(self, set2):
		""" Return the union of this set and 'set2'. """
		out = OurSet()
		for item in self:
			if item in set2:
				out.add(item)

		return out

	def intersection(self, set2):
		""" Return the intersection of this set and 'set2'. """
		out = OurSet()
		for item in self:
			if item not in out:
				out.add(item)
		for item in set2:
			if item not in out:
				out.add(item)

		return out

if __name__ == "__main__":
	os = OurSet()
	os.add(5)
	os.add(8)
	os.add_list([12, 10])
	os.add_list([])
	print(os)
	print(len(os))
	for item in os:
		print(item)

	os2 = OurSet()
	os2.add(5)
	os2.add(7)
	print(os.union(os2))
	print(os.intersection(os2))