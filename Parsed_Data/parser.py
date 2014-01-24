# to run the script, run "python parser.py <input filename> <output filename>"
# you may need to use "python3" instead of "python"

import random, sys

filename = sys.argv[1] # get the second command line argument, the filename
output_filename = sys.argv[2] # get third command line argument, the output filename
# f is an object representing the opened file
# If python gives UnicodeEncodeError, set errors='ignore' to ignore the malformed characters
# open is a builtin python function
f = open(filename, encoding='utf-8')
output = open(output_filename, 'w', encoding='utf-8')
parsed_input_lines = [] # an array
for line in f: # loop over every line in the file
	pair = line.split(' ', 1) # split on the first space, and not subsequent spaces. Pair = array of price and description
	pair[1] = pair[1].rstrip() # remove trailing whitespace (whitespace at the end)
	parsed_input_lines.append(pair) # add to end of array

# range and len are builtin python functions
length = len(parsed_input_lines) # get length
for i in xrange(length): # loop from 0 to length-1
	print('Parsing line', i) # print to console
	pair = parsed_input_lines[i]
	random_indices = {} # dictionary/hash
	if pair[1] != "":
                while len(random_indices) < 10:
                        rand = random.randrange(length)
                        x1 = float(parsed_input_lines[i][0])
                        x2 = float(parsed_input_lines[rand][0])
                        diff = abs (x1 - x2)
                        # integer from 0 to length of parsed_input_lines
                        # the .get method takes two arguments: the property to look up, and the value to return if the lookup fails
                        if rand == i or random_indices.get(rand, False) or (diff/x1 < .20 and diff/x2 < .20) or parsed_input_lines[rand][1] == "":
                                continue # restart at beginning of while,loop
                        else:
                                # mark the value in the hash as already found
                                random_indices[rand] = True
                for random_index in random_indices.keys():
                        selected_pair = parsed_input_lines[random_index]
                        # format inserts the arguments in order, in the string in place of {0}, {1}, etc
                        output_string = '{0} ^ {1} ^ {2} ^ {3}\n'.format(pair[0], selected_pair[0], pair[1], selected_pair[1])
                        # write the string to the file we opened earlier
                        output.write(output_string)
