#!/usr/bin/python3
f = open("input.txt", "r").read().split("\n")
count = 0
i = 0
while i < len(f) - 3:
	s1 = int(f[i]) + int(f[i+1]) + int(f[i+2])
	s2 = int(f[i+1]) + int(f[i+2]) + int(f[i+3])
	if (s1 < s2):
		count += 1
	i += 1
print(count)
