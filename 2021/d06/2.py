#!/usr/bin/python3
f = open("input.txt", "r").read().split(",")
for i, num in enumerate(f):
	f[i] = [int(f[i]), 1]

for day in range(0, 256):
	amount = 0
	for i, num in enumerate(f):
		if f[i][0] == 0:
			f[i] = [6, f[i][1]]
			amount += f[i][1]
		else:
			f[i][0] -= 1
	f.append([8, amount])

amount = 0
for i, num in enumerate(f):
	amount += f[i][1]

print(amount)
