__author__ = "Alexander Liang (all5dh)"

import os
import json

if __name__ == "__main__":
	dataFile = open('file_info.txt', 'r')
	dataJson = dataFile.read()
	data = json.loads(dataJson)

	item_list = os.listdir()

	for item in item_list:
		if not os.path.isdir(item):
			myFile = open(item, 'r')
			lines = 0
			for line in myFile:
				lines += 1

			if item not in data:
				print("data for file {} could not be found".format(item))

			elif lines != data[item]:
				print("file {} has been modified".format(item))

