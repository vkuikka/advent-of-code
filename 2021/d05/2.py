#!/usr/bin/python3
f = open("input.txt", "r").read().split("\n")
ceil = 0
for i, line in enumerate(f):
	f[i] = line.split(" -> ")
	f[i][0] = f[i][0].split(",")
	f[i][1] = f[i][1].split(",")
	ceil = max(ceil, int(f[i][0][0]))
	ceil = max(ceil, int(f[i][0][1]))
	ceil = max(ceil, int(f[i][1][0]))
	ceil = max(ceil, int(f[i][1][1]))
ceil = int(ceil) + 1

arr = []
for i in range(ceil):
	arr.append(list(range(ceil)))
for x in range(ceil):
	for y in range(ceil):
		arr[x][y] = 0

for i, line in enumerate(f):
	x = int(line[0][0])
	y = int(line[0][1])
	x_limit = int(line[1][0])
	y_limit = int(line[1][1])
	while (x != x_limit or y != y_limit):
		arr[y][x] += 1
		if x != x_limit:
			if (x < x_limit):
				x += 1
			else:
				x -= 1
		if y != y_limit:
			if (y < y_limit):
				y += 1
			else:
				y -= 1
	arr[y][x] += 1

count = 0
for line in arr:
	for num in line:
		if num > 1:
			count += 1
print(count)
