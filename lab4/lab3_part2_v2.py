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

	item_list = os.listdir()

	file_checksums = {}
	out = []
	out.append(os.path.realpath(__file__))

	for item in item_list:
		if not os.path.isdir(item):
			checksum = get_file_checksum(item)

			file_checksums[item] = checksum

	out.append(file_checksums)

	fileOut = open('file_checksums.txt', 'w')
	fileOut.write(json.dumps(out[1]))
	fileOut.close()
