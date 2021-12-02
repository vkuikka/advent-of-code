#!/usr/bin/python3
f = open("input.txt", "r").read().split("\n")
x = 0
y = 0
aim = 0
for j, line in enumerate(f):
	num = [int(i) for i in line.split() if i.isdigit()][0]
	if line[0] == 'f':
		x += num
		y += aim * num
	if line[0] == 'd':
		aim += num
	if line[0] == 'u':
		aim -= num
print(x * y)
