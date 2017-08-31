
def maxmin(list):
	""" Return a tuple containing the largest and smallest values in the list. """
	if len(list) <= 0:
		return None
	
	big = list[0]
	small = list[1]

	for item in list:
		if item > big:
			big = item;
		if item < small:
			small = item;

	return (big, small)

def common_items(list1, list2):
	""" Return a list of common items between list1 and list2. """
	out = []

	for item in list1:
		if item in list2 and not item in out:
			out.append(item)

	return out

def notcommon_items(list1, list2):
	""" Return a list of items which are not in common between list1 and list2. """
	out = []

	for item in list1:
		if item not in list2 and item not in out:
			out.append(item)
	for item in list2:
		if item not in list1 and item not in out:
			out.append(item)

	return out

def count_list_items(list):
	""" Return a dictionary containing the number of occurances of each item in the list. """
	out = {}

	for item in list:
		if item in out:
			out[item] += 1
		else:
			out[item] = 1

	return out

if __name__ == "__main__":
	print(maxmin(['A', 'B', 'Z']))
	print(maxmin([5, 3, 1, 23, 12]))

	print(common_items([1, 3, 5, 7, 9, 3, 3, 3], [1, 2, 3, 4, 5, 3, 3, 3]))
	print(common_items([1, 'A', 3.14, 'hello world'], ['3.14', 'hello world', 1, 'A']))

	print(notcommon_items([1, 3, 3, 3, 5, 7, 9, 11], [1, 2, 2, 3, 3, 3, 4, 5]));

	print(count_list_items([1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 'a']))
