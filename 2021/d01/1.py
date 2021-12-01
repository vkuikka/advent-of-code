#!/usr/bin/python3
f = open("input.txt", "r").read().split("\n")
count = 0
for i, _ in enumerate(f):
	if i != 0 and int(f[i-1]) < int(f[i]):
		count += 1
print(count)
