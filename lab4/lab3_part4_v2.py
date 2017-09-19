__author__ = "Alexander Liang (all5dh)"

import json
from Crypto.Cipher import AES
from Crypto import Random

if __name__ == "__main__":
	key = input("What is the key: ")
	message = input("What is the message: ")

	iv = Random.new().read(AES.block_size)

	aes = AES.new(key, AES.MODE_ECB, iv)
	cipher_text = iv + aes.encrypt(message)

	with open('secret_aes.txt', 'wb') as myFile:
		myFile.write(cipher_text)