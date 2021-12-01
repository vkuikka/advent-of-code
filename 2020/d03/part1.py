#!/usr/bin/env python3
input = open("input.txt", "r").read()
splitted = input.split('\n')
right = 0
count = 0
for i, line in enumerate(splitted):
	if (line[right] == '#'):
		count += 1
	right += 3
	if (right >= len(line)):
		right -= len(line)
print(count)
