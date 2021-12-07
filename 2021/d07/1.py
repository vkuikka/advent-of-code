#!/usr/bin/python3
f = open("input.txt", "r").read().split(",")
for i, num in enumerate(f):
	f[i] = int(num)
total_min = 0
for align in range(len(f)):
	total = 0
	for num in f:
		total += abs(num - align)
	if total < total_min or total_min == 0:
		total_min = total
print(total_min)
