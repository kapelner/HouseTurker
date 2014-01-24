import random, sys, math

# The inputs have to be in the form, Ratio, Right = 1, Wrong = 0, in ascending order
# 3 inputs, fileinput, fileoutput, bin size

filename = sys.argv[1]
outputname = sys.argv[2]
bin = sys.argv[3]

f = open(filename, encoding='utf-8')
output = open(outputname, 'w', encoding='utf-8')

inputarray = []
for line in f:
	pair = line.split(",", -1)
	pair[len(pair) - 1] = pair[len(pair) - 1].rstrip()
	inputarray.append(pair)

length = len(inputarray)

counter = 0

totalRatio = 0

totalCorrect = 0

for i in range(length):
	pair = inputarray[i]
	ratio = float(pair[0])
	corr = int(pair[1])
	if counter == int(bin):
		output.write(str(totalRatio) + "," + str(totalCorrect) + "," + str(counter) + "\n")
		counter = 1
		totalRatio = ratio
		totalCorrect = corr
	else:	
		counter = counter + 1
		totalRatio = totalRatio + ratio
		totalCorrect = totalCorrect + corr
	print(totalRatio)

output.write(str(totalRatio) + "," + str(totalCorrect) + "," + str(counter) + "\n")

f.close()
output.close()