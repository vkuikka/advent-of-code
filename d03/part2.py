#!/usr/bin/env python3
def check_slope(right, down):
	pos = 0
	count = 0
	for i, line in enumerate(splitted):
		if (i % down) == 0:
			if (line[pos] == '#'):
				count += 1
			pos += right
			if (pos >= len(line)):
				pos -= len(line)
	return count

input = open("input.txt", "r").read()
splitted = input.split('\n')
count = check_slope(1, 1)
count *= check_slope(3, 1)
count *= check_slope(5, 1)
count *= check_slope(7, 1)
count *= check_slope(1, 2)
print(count)
