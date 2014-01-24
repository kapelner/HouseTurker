import random, sys

# The input has to be in the form Worker ID + (Answer 1 2 3 4 5, Right answer 1 2 3 4 5)

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

workerID = ""

correctCounter = 0;

numberHITCounter = 0;

for i in range(length):
	pair = inputarray[i]
	if pair[0] == workerID:
		for j in range(5):
			numberHITCounter = numberHITCounter + 1
			if pair[j + 1] == pair[j + 6]:
				correctCounter = correctCounter + 1
	else:
		if i != 0:
			output.write(str(numberHITCounter) + "^" + str(correctCounter) + "\n")
		numberHITCounter = 0
		correctCounter = 0;
		workerID = pair[0]
		for j in range(5):
			numberHITCounter = numberHITCounter + 1
			if pair[j + 1] == pair[j + 6]:
				correctCounter = correctCounter + 1

output.write(str(numberHITCounter) + "^" + str(correctCounter) + "\n")

f.close()
output.close()