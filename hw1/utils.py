import math

def distanceBetween(p1, p2):
	out = (p1.x - p2.x)**2 + (p1.y - p2.y)**2;
	out = math.sqrt(out);
	return out;


class point:
	def __init__(self, x, y, category = ""):
		self.x = x;
		self.y = y;
		self.category = category;
		self.distance = math.inf;

	def __str__(self):
		#return '(' + str(self.x) + ', ' + str(self.y) + '): ' + self.category;
		return "({}, {}): {}".format(self.x, self.y, self.category);

	# Why would you do this python????
	def __repr__(self):
		return self.__str__();


def readFile(filename, M):
	# list which holds all of the classified values
	classified = [];

	try :
		myfile = open(filename, 'r');
		count = 0;
		for line in myfile:
			count += 1;
			if (count > M):
				break;
			data = line.split();
			classified.append(point(float(data[1]), float(data[2]), str(data[0])));
		if (count < M):
			print("Could not read {} values; only {} were found.".format(M, count));
	except IOError:
		print("File Not Found");

	return classified;


def answerPart1(classified, k):
	for i in range(k):
		p = classified[i];

		print("{} {} {} {}".format(p.category, p.x, p.y, p.distance));


def answerPart2(electoral_college, me):
	biggest = 0;
	biggestCategory = "";
	for key in electoral_college.keys():
		if (electoral_college[key] > biggest):
			biggestCategory = key;

	print("Data item ({}, {}) assigned to: {}".format(me.x, me.y, biggestCategory));


def answerPart3(electoral_college, distances):
	for key in electoral_college.keys():
		print("Average distance to {} items: {}".format(key, distances[key]/electoral_college[key]));