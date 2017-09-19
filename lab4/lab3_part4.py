__author__ = "Alexander Liang (all5dh)"

import json
from Crypto.Cipher import DES

if __name__ == "__main__":
	key = input("What is the key: ")
	message = input("What is the message: ")

	des = DES.new(key, DES.MODE_ECB)
	cipher_text = des.encrypt(message)

	with open('secret.txt', 'wb') as myFile:
		myFile.write(cipher_text)