#!/usr/bin/python3
f = open("input.txt", "r").read().split(",")
for i, num in enumerate(f):
	f[i] = int(num)
total_min = 0
for align in range(len(f)):
	total = 0
	for num in f:
		if num != align:
			num = abs(num - align)
			# https://en.wikipedia.org/wiki/Triangular_number
			total += num * (num + 1) / 2
	if total < total_min or total_min == 0:
		total_min = total
print(int(total_min))
