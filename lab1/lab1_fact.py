# something something semicolons are unpythonic something something
import math 

# is recursion really the best way to do this??
# TODO: Assumes n is an integer
def factorial1(n):
	if n < 0:
		raise ValueError
	if n == 0:
		return 1
	else:
		return (n) * factorial1(n-1)

def factorial2(n):
	answers = []
	for i in range(n+1):
		answers.append(factorial1(i))
	return answers

# Test factorial1(n) against math.factorial(n)
def test_fact1():
	for i in range(11):
		print("Testing n = {}: ".format(i))
		assert math.factorial(i) == factorial1(i)

	print("Testing negative n: ")
	try:
		factorial1(-1)
	except ValueError:
		print("Success")
	except:
		print("Fail")

if __name__ == "__main__":
	test_fact1()

	# Test factorial2(n)
	f1Answers = []
	for i in range(11):
		f1Answers.append(factorial1(i))
	assert factorial2(10) == f1Answers
