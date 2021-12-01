#!/usr/bin/env python3
input = open("input.txt", "r").read()
splitted = input.split('\n')
for i, line in enumerate(splitted):
	splitted[i] = line.split(' ')
	splitted[i][0] = splitted[i][0].split('-')
valid_count = 0
for line in splitted:
	index1 = int(line[0][0]) - 1
	index2 = int(line[0][1]) - 1
	if ((index1 < len(line[2]) and index2 < len(line[2])) and 
		((line[1][0] == line[2][index1]) ^ (line[1][0] == line[2][index2]))):
		valid_count += 1
print(valid_count)
