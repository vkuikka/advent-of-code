#!/usr/bin/env python3
from colorama import init
init(autoreset=False)

def count_children(bags, start_color, depth):
	# col = str('   ' * depth)
	col = '\033[' + str(31 + depth) + 'm' + str('   ' * depth)
	try:
		count = bags[start_color]["child_count"]
		print(col, start_color, count, "\t\tfrom saved!")
		return count
	except:
		print(col, start_color, " -> ", bags[start_color])
		count = 0
		for color in bags[start_color]:
			if color == "otherbags.":
				count = 0
				break
			amount = int(bags[start_color][color])
			tmp = count_children(bags, color, depth + 1)
			count += tmp * amount + amount

	bags[start_color]["child_count"] = count
	print(col, start_color, count)
	print()
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

count = count_children(bags, "shinygold", 0)

print(count)

# 34988