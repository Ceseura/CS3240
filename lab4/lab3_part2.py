__author__ = "Alexander Liang (all5dh)"

import os
import json

if __name__ == "__main__":

	item_list = os.listdir()

	num_lines = {}
	out = []
	out.append(os.path.realpath(__file__))

	for item in item_list:
		if not os.path.isdir(item):
			myfile = open(item, 'r')
			lines = 0
			for line in myfile:
				lines += 1
			num_lines[item] = lines 

	out.append(num_lines)

	fileOut = open('file_info.txt', 'w')
	fileOut.write(json.dumps(out[1]))

# comment