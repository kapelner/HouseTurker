import random, sys, math

# The inputs have to be 10 columns of prices

filename = sys.argv[1]
outputname = sys.argv[2]

f = open(filename, encoding='utf-8')
output = open(outputname, 'w', encoding='utf-8')

inputarray = []
for line in f:
	pair = line.split(",", -1)
	pair[len(pair) - 1] = pair[len(pair) - 1].rstrip()
	inputarray.append(pair)

length = len(inputarray)

def getWord(n):
	n = float(n)
	# 1 mil to 9.99 mil
	if n >= 1000000 and n <= 9999999:
		return str(round(n / 1000000.0, 2)) + " Mil"
	# 10 mil to 99.9 mil
	elif n >= 10000000 and n <= 99999999:
		return str(round(n / 1000000.0, 1)) + " Mil"
	# 100 mil to 999. mil
	elif n >= 100000000 and n <= 999999999:
		return str(int(round(n / 1000000.0, 0))) + " Mil"
	# 100k to 999k
	elif n >= 100000 and n <= 999999:
		return str(int(round(n / 1000.0, 0))) + " K"
	# 10k to 99k
	elif n >= 10000 and n <= 99999:
		return str(round(n / 1000.0, 1)) + " K"
	# 1k to 9k
	elif n >= 1000 and n <= 9999:
		return str(round(n / 1000.0, 1)) + " K"
	else:
		return "NA"

for i in range(length):
	pair = inputarray[i]
	for j in range(len(pair) - 1):
		output.write(str(pair[j]) + "," + str(getWord(pair[j])) + ",")
	output.write(str(pair[len(pair) - 1]) + "," + str(getWord(pair[len(pair) - 1])) + "\n")

output.close()