import random, sys

filename = sys.argv[1]
output_filename = sys.argv[2]

f = open(filename, encoding='utf-8')
output = open(output_filename, 'w', encoding='utf-8')
inputarray  = []
for line in f:
	pair = line.split("^", -1)
	pair[3] = pair[3].rstrip()
	inputarray.append(pair)

length = len(inputarray)
random.shuffle(inputarray)

for i in range(length):
	pair = inputarray[i]
	print('Parsing line', i)
	output_string = '{0} ^ {1} ^ {2} ^ {3}\n'.format(pair[0], pair[1], pair[2], pair[3])
	output.write(output_string)