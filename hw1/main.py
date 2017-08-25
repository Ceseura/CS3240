import math # this isn't already here???

def distanceBetween(p1, p2):
	out = (p1[0] + p2[0])**2 + (p1[1] + p2[1])**2
	out = math.sqrt(out);

	return out;

class point:
	def __init__(self, x, y, cat = ""):
		self.x = x;
		self.y = y;
		self.cat = cat;

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + '): ' + self.cat;

	# Why would you do this python????
	def __repr__(self):
		return self.__str__();

k = input("input k: ");
print(k);
M = input("input M: ");
print(M);
filename = input("input filename: ");
print(filename);

# list which holds all of the classified values
classified = [];
try :
	myfile = open(filename, 'r');
	for line in myfile:
		data = line.split();
		classified.append(point(float(data[1]), float(data[2]), str(data[0])));
except IOError:
	print("File Not Found");
	# TODO: Consider asking for a new filename?

print(classified);


# Consider putting all this in a function for readability

# list which holds all of the unclassified values
unclassified = []; 

getting = True;
while (getting): 
	data = input("input x y: ");

	print(data);
	data = data.split();

	# check if input is invalid
	if (len(data) < 2):
		print("invalid input. Please input an x, y pair in the format: 'x y'");
	else: 
		# parse point into a point object with empty category
		p = point(float(data[0]), float(data[1]));

		# stop taking input if you get '1 1'

		if (p.x == 1 and p.y == 1):
			getting = False;
		else:
			unclassified.append(p);
		
print(unclassified);

# now do some calculus shit




