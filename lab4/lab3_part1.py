__author__ = "Alexander Liang (all5dh)"

from Crypto.Hash import SHA256

if __name__ == "__main__":

	running = True
	confidential_data = {}
	while running:
		username = input("Input a username: ")

		if username == "":
			running = False
		else:
			password = input("password: ")
			hash_password = SHA256.new(password.encode('utf-8')).hexdigest()
			confidential_data[username] = hash_password

	print(confidential_data)

	while True:
		user = input("        username: ")
		password = input("        password: ")
		hash_password = SHA256.new(password.encode('utf-8')).hexdigest()
		if user not in confidential_data:
			print("User not found")
		else:
			if confidential_data[user] == hash_password:
				print("login succeeds")
			else:
				print("login fails")

