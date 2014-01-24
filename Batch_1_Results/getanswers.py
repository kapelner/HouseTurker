import random, sys

filename = sys.argv[1]
outputname = sys.argv[2]


f = open(filename, encoding='utf-8')
output = open(outputname, 'w', encoding='utf-8')

inputarray  = []
for line in f:
	pair = line.split("^", -1)
	inputarray.append(pair)

length = len(inputarray)

counter = 0;

for i in range(length):
	pair = inputarray[i];
	for j in range(5):
		internalcounter = 0;
		if pair[j] == pair[j + 5]
			counter = counter + 1; 
			internalcounter = internalcounter + 1;
			output.write(str(internalcounter) + '\n')