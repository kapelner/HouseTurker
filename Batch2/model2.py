import random, sys, re, string

# takes in a file that has words as descriptions

filename = sys.argv[1]
outputname = sys.argv[2]

f = open(filename, encoding='utf-8')
output = open(outputname, 'w', encoding='utf-8')

#counter to keep track of the values. Each word has an index associated with it
counter = 0

#creates the new dictionary that will store the words along with its indecies
tokens = dict()

#loop to handle the adding to dictionary
for line in f:
	# for each line in the file, split the string by space character
	words = line.split()
	for w in words:
		# convert character to lowercase
		w = w.lower()
		w = w.translate(string.maketrans("",""), string.punctuation)
		if not(w in tokens):
			tokens[w] = counter
			counter += 1

for key, value in tokens.items():
	print("key is " + key + " value is " + str(value))
	output.write(key + " " + str(value) + "\n")

print(len(tokens))
f.close()
output.close()