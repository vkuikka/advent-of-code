#!/usr/bin/python3
f = open("input.txt", "r").read().split("\n")
for i, line in enumerate(f):
	f[i] = list(line)

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
match = {'{':'}', '(':')', '[':']', '<':'>'}
rmatch = {'}':'{', ')':'(', ']':'[', '>':'<'}
queue = []
total = 0
for i, line in enumerate(f):
	for j, c in enumerate(line):
		if c in match:
			queue.append(c)
		else:
			end = queue[-1]
			if rmatch[c] == end:
				queue.pop()
			else:
				total += points[c]
				break
print(total)