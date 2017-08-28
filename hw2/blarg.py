
def notcommon_items(list1, list2):
	out = []

	for item in list1:
		if item not in list2 and item not in out:
			out.append(item)
	for item in list2:
		if item not in list1 and item not in out:
			out.append(item)

	return out

def count_list_items(list):
	out = {}

	for item in list:
		if item in out:
			out[item] += 1
		else:
			out[item] = 1

	return out

if __name__ == "__main__":
	print(notcommon_items([1, 3, 3, 3, 5, 7, 9, 11], [1, 2, 2, 3, 3, 3, 4, 5]));
	print(count_list_items([1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 'a']))