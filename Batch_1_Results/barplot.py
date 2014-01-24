import random, sys, math

# The inputs have to be in the form, Ratio, Right = 1, Wrong = 0

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

correctArr = [0] * 11

totalArr = [0] * 11

for i in range(length):
	pair = inputarray[i]
	ratio = float(pair[0])
	ratio = math.log(ratio, 2)
	bin = math.trunc(ratio)
	# print(str(ratio) + " " + str(bin) + "\n")
	if int(pair[1]) == 1:
		if bin >= 10:
			correctArr[10] = correctArr[10] + 1
		else:
			correctArr[bin] = correctArr[bin] + 1
	if bin >= 10:
		totalArr[10] = totalArr[10] + 1
	else:
		totalArr[bin] = totalArr[bin] + 1

for j in range(len(totalArr)):
	# print(str(totalArr[j]))
	if totalArr[j] != 0:
		percent = correctArr[j] / totalArr[j]
		# print("The " + str(j) + " th one: " + str(percent) + "\n")
		output.write(str(j) + "," + str(percent) + "," + str(correctArr[j]) + "," + str(totalArr[j]) + "\n")

f.close()
output.close()