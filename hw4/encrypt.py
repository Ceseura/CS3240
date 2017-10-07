# Use AES for the symmetric encryption, and RSA for assymetric encryption
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random

def secret_string(data, key):
	''' Takes a string and RSA public key as input, returns the encrypted string'''
	cipher = PKCS1_v1_5.new(key)
	cipher_text = cipher.encrypt(data.encode())
	print(cipher_text)
	return cipher_text
	
### TODO: error checking, make sure filename formatting is correct
### TODO: Try encrypting non text files?
def enc_file(filename, key):
	''' Takes a filename and an AES symmetric key, creates a new, encrypted file. Returns true if the operation was successful. '''
	with open(filename, 'rb') as dfile, open(filename + '.enc', 'wb') as eFile:
		running = True 
		while running:
			block = dfile.read(1024 * AES.block_size)
			# stop if you run out of stuff to read
			if len(block) == 0:
				running = False
			else:
				# add padding if necessary
				while len(block) % AES.block_size != 0:
					block += b' '

				cipher = AES.new(key, AES.MODE_ECB)
				msg = cipher.encrypt(block)
				eFile.write(msg)
		return True

def decrypt_file(filename, key):
	''' Takes a filename and an AES symmetric key, creates a new, decrypted file. Returns true if the operation was successful. '''
	with open(filename, 'rb') as efile, open('DEC' + filename[:-4], 'wb') as dfile:
		running = True
		while running:
			block = efile.read(1024 * AES.block_size)
			# stop if you run out of stuff to read
			if len(block) == 0:
				running = False
			else:
				# Shouldn't need to add padding if the file has been encrypted correctly
				cipher = AES.new(key, AES.MODE_ECB)
				msg = cipher.decrypt(block)
				dfile.write(msg)


def test_secret_string():
	key = RSA.generate(1024)
	publicKey = key.publickey()
	message = "hello I am message"
	print(message)
	encrypted = secret_string(message, publicKey)

	de = PKCS1_v1_5.new(key)
	decrypted = de.decrypt(encrypted, key)
	print(decrypted)

def test_encrypt_file():
	with open("testFile.txt", 'w') as myFile:
		myFile.write("A super secret document containing highly confidential information.")

	key = b'Sixteen byte key'

	enc_file("testFile.txt", key)

def test_decrypt_file():
	key = b'Sixteen byte key'

	decrypt_file("testFile.txt.enc", key)

test_decrypt_file()
