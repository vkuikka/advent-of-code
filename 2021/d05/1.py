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
	minx = int(min(float(line[0][0]), float(line[1][0])))
	maxx = int(max(float(line[0][0]), float(line[1][0])))
	miny = int(min(float(line[0][1]), float(line[1][1])))
	maxy = int(max(float(line[0][1]), float(line[1][1])))
	if minx == maxx or miny == maxy:
		for x in range(minx, maxx + 1):
			for y in range(miny, maxy + 1):
				arr[y][x] += 1

count = 0
for x in range(ceil):
	for y in range(ceil):
		if (arr[x][y] > 1):
			count += 1
print(count)
