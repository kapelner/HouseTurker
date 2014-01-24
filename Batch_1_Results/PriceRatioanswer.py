import random, sys, math

# The inputs have to be in the form, Price 1, Price 2, Worker Answer, Right Answer x 5, gives ratios

filename = sys.argv[1]
outputname = sys.argv[2]

f = open(filename, encoding='utf-8')
output = open(outputname, 'w', encoding='utf-8')

inputarray  = []
for line in f:
	pair = line.split("^", -1)
	pair[len(pair) - 1] = pair[len(pair) - 1].rstrip()
	inputarray.append(pair)

length = len(inputarray)

correctCounter = 0;

for i in range(length):
	pair = inputarray[i]
	for j in range(5):
		ratio = -1;
		x1 = int(pair[4 * j])
		x2 = int(pair[4 * j + 1])
		if x1 > x2:
			ratio = x1 / x2
		else:
			ratio = x2 / x1
		correct = 0
		if pair[4 * j + 2] == pair [4 * j + 3]:
			correct = 1
		# print("The Price " + str(j) + " is: " + str(pair[4 * j])
		# + "The Price " + str(j) + " 2 is: " + str(pair[4 * j + 1])
		# + "The Ratio" + str(j) + " is: " + str(ratio)
		# + "The Input " + str(j) + " is: " + pair[4 * j + 2]
		# + "The Answer " + str(j) + " is: " + pair[4 * j + 3]
		# + "The Correctness" + str(j) + " is: " + str(correct) + "\n")
		# if math.log(ratio,2) > 8.5:
			# print(str(x1) + " " + str(x2) + " " + str(math.log(ratio,2)))
		output.write(str(ratio) + "^" + str(correct) + "\n")

f.close()
output.close()