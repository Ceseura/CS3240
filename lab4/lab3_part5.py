__author__ = "Alexander Liang (all5dh)"

from Crypto.Cipher import DES

if __name__ == "__main__":
	key = input("What is the key: ")

	des = DES.new(key, DES.MODE_ECB)

	with open('secret.txt', 'rb') as inFile:
		encoded_message = inFile.read()
		message = des.decrypt(encoded_message)
		print(message)
