#!/usr/bin/python3
def num_in_match():
	match = False
	for k, n in enumerate(f[0][0]):
		if k > test_i:
			break
		if n == num:
			match = True
	return match

def print_win():
	count = 0
	for x in range(0, 5):
		for y in range(0, 5):
			if marks[x][y] != 1:
				count += int(block[x][y])
	res = count * int(test)
	print(count * int(test))

# I removed double spaces from input
f = open("input.txt", "r").read().split("\n\n")
for i, line in enumerate(f):
	f[i] = line.rstrip().split("\n")
for i, line in enumerate(f):
	for j, row in enumerate(line):
		row = row.strip()
		if i == 0:
			f[i][j] = row.split(",")
		else:
			f[i][j] = row.split(" ")

for test_i, test in enumerate(f[0][0]):
	for block_i, block in enumerate(f[1:]):
		marks = []
		for _ in range(0, 5):
			marks.append([0, 0, 0, 0, 0])

		for i, row in enumerate(block):
			for j, num in enumerate(row):
				if num_in_match():
					marks[i][j] = 1

		for i in range(0, 5):
			row_win = True
			col_win = True
			for j in range(0, 5):
				if marks[i][j] != 1:
					row_win = False
				if marks[j][i] != 1:
					col_win = False
			if row_win or col_win:
				print_win()
				exit()
