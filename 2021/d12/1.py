#!/usr/bin/python3
total = 0
paths = []

def check_connected(this, distance, inroom, visited):
	distance = 0
	visited = visited.copy()
	visited.append(this["name"])
	visits = visited.count(this["name"])
	if visits > 1 and this["big"] == False:
		return
	if f[inroom][0]["name"] == "end" or f[inroom][1]["name"] == "end":
		s = "".join(visited)
		if s not in paths:
			global total
			total += 1
			paths.append(s)
			print(" ", total, "\t", ",".join(visited), end="\r")
		return
	for i, line in enumerate(f):
		if this["name"] == line[0]["name"]:
			check_connected(line[1], distance, i, visited)
		elif this["name"] == line[1]["name"]:
			check_connected(line[0], distance, i, visited)

f = open("input.txt", "r").read().split("\n")
for i, row in enumerate(f):
	row = row.split("-")
	f[i] = row
	for j in range(2):
		f[i][j] = {"name":f[i][j], "big":False, "visited":False}
		if f[i][j]["name"].isupper():
			f[i][j]["big"] = True
		else:
			f[i][j]["big"] = False

thisname = "start"
visited = []
for i, line in enumerate(f):
	if line[0]["name"] == "start":
		check_connected(line[0], 0, i, visited)
	elif line[1]["name"] == "start":
		check_connected(line[1], 0, i, visited)
print()
print(total)
