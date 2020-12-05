#!/usr/bin/env python3
input = open("input.txt", "r").read()
splitted = input.split('\n')

all_id = []
for line in splitted:
	row_min = 0
	row_max = 128
	col_min = 0
	col_max = 8
	for i, c in enumerate(line):
		if i < 7:
			if c == 'F':
				row_max = int((row_max + row_min) / 2)
			elif c == 'B':
				row_min = int((row_max + row_min) / 2 + 0.1)
		else:
			if c == 'L':
				col_max = int((col_max + col_min) / 2)
			if c == 'R':
				col_min = int((col_max + col_min) / 2 + 0.1)
	all_id.append(row_min * 8 + col_min)

highest = all_id[0]
for num in all_id:
	if num > highest:
		highest = num
print(highest)
