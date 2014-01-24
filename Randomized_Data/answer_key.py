import random, sys

filename = sys.argv[1]
outputname = sys.argv[2]


f = open(filename, encoding='utf-8')
output = open(outputname, 'w', encoding='utf-8')

inputarray  = []
for line in f:
	pair = line.split("^", -1)
	pair[3] = pair[3].rstrip()
	inputarray.append(pair)

length = len(inputarray)

answerarray = []

for i in range(length):
	pair = inputarray[i]
	if random.random() > .50:
		pair.append("A")
		answerarray.append(pair)
	else:
		temp = pair[0]
		pair[0] = pair[1]
		pair[1] = temp
		pair.append("B")
		answerarray.append(pair)

length2 = int (len(answerarray) / 5)

for i in range(length2):
	output_string = ""
	for j in range(5):
		index = 5 * i + j
		pair = answerarray[index]
		output_string += '^{0}^{1}^{2}^{3}^{4}'.format(pair[0], pair[1], pair[2], pair[3], pair[4])
		print ("parsing string ", index)
	output_string += "\n"
	output.write(output_string)