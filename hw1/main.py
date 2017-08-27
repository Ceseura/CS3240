# Alexander Liang (all5dh@virginia.edu)

import utils
from utils import point

k = int(input("input k, the number of nearest neighbors who get a vote: "));
print(k);

M = int(input("input M, the number of values to be read from the datafile: "));
print(M);

# TODO: Assumes contents of file are valid and will be formatted correctly
# python doesn't have do-while?????
getting = True;
while(getting):
	filename = input("input filename containing classified points: ");

	classified = utils.readFile(filename, M);

	# Keep asking until you get a non-empty file
	if (len(classified) != 0):
		getting = False;


getting = True;
while (getting): 
	data = input("input x y to be classified: ");
	data = data.split();

	# check if input is invalid
	if (len(data) < 2):
		print("invalid input. Please input an x, y pair in the format: 'x y'");
	else: 
		# parse point into a point object with empty category
		me = point(float(data[0]), float(data[1]));

		# stop taking input if you get '1 1'
		if (me.x == 1 and me.y == 1):
			getting = False;
			break;


	# now do some calculus shit

	# Calculate distance to each classified point
	for item in classified:
		item.distance = utils.distanceBetween(me, item);

	# Sort classified by distance
	classified.sort(key=lambda x: x.distance);

	# Poll the closest k classified points
	electoral_college = {};
	distances = {};
	for i in range(k):
		if (classified[i].category in electoral_college):
			electoral_college[classified[i].category] += 1;
			distances[classified[i].category] += classified[i].distance;
		else:
			electoral_college[classified[i].category] = 1;
			distances[classified[i].category] = classified[i].distance;

	utils.answerPart1(classified, k);
	utils.answerPart2(electoral_college, me);
	utils.answerPart3(electoral_college, distances);


