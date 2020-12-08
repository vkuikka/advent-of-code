#!/usr/bin/env python3
def count_children(bags, start_color, depth):
	try: return bags[start_color]["child_count"]
	except:
		count = 0
		for color in bags[start_color]:
			if color == "otherbags.": # "no other bags."
				break
			amount = int(bags[start_color][color])
			tmp = count_children(bags, color, depth + 1)
			count += tmp * amount + amount
	bags[start_color]["child_count"] = count
	return count

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
print(count_children(bags, "shinygold", 0))
