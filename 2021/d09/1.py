#!/usr/bin/python3
f = open("input.txt", "r").read().split("\n")
for i, row in enumerate(f):
	f[i] = list(row)
	for j, num in enumerate(row):
		f[i][j] = int(num)

total = 0
for i, line in enumerate(f):
	for j, num in enumerate(line):
		left = f[i][j-1] if j > 0 else 10
		right = f[i][j+1] if j < len(line)-1 else 10
		top = f[i-1][j] if i > 0 else 10
		bot = f[i+1][j] if i < len(f)-1 else 10
		if num < left and num < top and num < right and num < bot:
			total += num + 1
print(total)
