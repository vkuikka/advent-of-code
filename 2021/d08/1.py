#!/usr/bin/python3
f = open("input.txt", "r").read().split("\n")
for i, num in enumerate(f):
	f[i] = f[i].split("|")
	f[i][0] = f[i][0].strip()
	f[i][1] = f[i][1].strip()
	f[i][0] = f[i][0].split(" ")
	f[i][1] = f[i][1].split(" ")

total = 0
for i, line in enumerate(f):
	for each in line[1]:
		res = len(each)
		if len(each) in (2, 4, 3, 7):
			total += 1
print(total)
