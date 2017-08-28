def maxmin(list):
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
	out = []

	for item in list1:
		if item in list2 and not item in out:
			out.append(item)

	return out

if __name__ == "__main__":
	print(maxmin(['A', 'B', 'Z']))
	print(maxmin([5, 3, 1, 23, 12]))

	print(common_items([1, 3, 5, 7, 9, 3, 3, 3], [1, 2, 3, 4, 5, 3, 3, 3]))
	print(common_items([1, 'A', 3.14, 'hello world'], ['3.14', 'hello world', 1, 'A']))