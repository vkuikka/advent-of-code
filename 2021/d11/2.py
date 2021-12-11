#!/usr/bin/python3

def flash(row, col):
	total = 0
	f[row][col][0] = 0
	f[row][col][1] = 1
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == 0 and j == 0:
				continue
			if row + i >= 0 and col + j >= 0 and row + i < len(f) and col + j < len(f):
				if f[row + i][col + j][1] == 0:
					f[row + i][col + j][0] += 1
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == 0 and j == 0:
				continue
			if row + i >= 0 and col + j >= 0 and row + i < len(f) and col + j < len(f):
				if f[row + i][col + j][0] > 9 and \
				f[row + i][col + j][1] == 0:
					total += flash(row + i, col + j)
	return total + 1

f = open("input.txt", "r").read().split("\n")
for i, row in enumerate(f):
	f[i] = list(row)
	for j, num in enumerate(row):
		f[i][j] = [int(num), 0]

flashes = 0
for step in range(1000):
	for row, line in enumerate(f):
		for col, num in enumerate(line):
			f[row][col][0] += 1
	for row, line in enumerate(f):
		for col, num in enumerate(line):
			if f[row][col][0] > 9:
				flashes += flash(row, col)
	count = 0
	for row, line in enumerate(f):
		for col, num in enumerate(line):
			if f[row][col][1] == 1:
				count += 1
				f[row][col][1] = 0
	if count == len(f) * len(f):
		print(step + 1)
		exit()
