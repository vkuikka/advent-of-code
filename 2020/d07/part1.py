#!/usr/bin/env python3
def find_col(find_this, bags, start_color):
	for color in bags[start_color]:
		if color == find_this:
			return True
		else:
			try:
				if find_col(find_this, bags, color):
					return True
			except:
				pass
	return False

input = open("input.txt", "r").read()
text = input.split('\n')

bags = {}
for i, line in enumerate(text):
	line = line.split(' ')
	line_i = 4
	line_data = {}
	while line_i < len(line):
		amount = line[line_i]
		name = line[line_i + 1] + line[line_i + 2]
		line_data[name] = amount
		line_i += 4
	bags[line[0] + line[1]] = line_data

count = 0
target = "shinygold"
for bag in bags:
	if find_col(target, bags, bag):
		count += 1
print(count)
