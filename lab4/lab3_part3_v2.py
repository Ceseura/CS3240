__author__ = "Alexander Liang (all5dh)"

import os
import json
from Crypto.Hash import MD5

def get_file_checksum(filename):
	h = MD5.new()
	chunk_size = 8192
	with open(filename, 'rb') as f:
		while True:
			chunk = f.read(chunk_size)
			if len(chunk) == 0:
				break
			h.update(chunk)
	return h.hexdigest()


if __name__ == "__main__":
	dataFile = open('file_checksums.txt', 'r')
	dataJson = dataFile.read()
	data = json.loads(dataJson)
	dataFile.close()

	item_list = os.listdir()

	for item in item_list:
		if not os.path.isdir(item):
			checksum = get_file_checksum(item)

			if item not in data:
				print("data for file {} could not be found".format(item))

			elif checksum != data[item]:
				print("file {} has been modified".format(item))

