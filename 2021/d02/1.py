#!/usr/bin/python3
f = open("input.txt", "r").read().split("\n")
x = 0
y = 0
for j, line in enumerate(f):
	num = [int(i) for i in line.split() if i.isdigit()][0]
	if line[0] == 'f':
		x += num
	if line[0] == 'd':
		y += num
	if line[0] == 'u':
		y -= num
print(x * y)
