#!/usr/bin/python3

def remove_errors(f):
	for i, line in enumerate(f):
		for j, c in enumerate(line):
			if c in match:
				queue.append(c)
			else:
				end = queue[-1]
				if rmatch[c] == end:
					queue.pop()
				else:
					total = points[c]
					f.pop(i)
					total += remove_errors(f)
					return (total)
	return (0)

f = open("input.txt", "r").read().split("\n")
for i, line in enumerate(f):
	f[i] = list(line)

points = {')': 1, ']': 2, '}': 3, '>': 4}
match = {'{':'}', '(':')', '[':']', '<':'>'}
rmatch = {'}':'{', ')':'(', ']':'[', '>':'<'}
total = []
queue = []
remove_errors(f)
for i, line in enumerate(f):
	for j, c in enumerate(line):
		if c in rmatch:
			k = j
			while k >= 0:
				if line[k] == rmatch[c]:
					line[k] = ' '
					line[j] = ' '
					break
				k -= 1
	linetotal = 0
	for i, c in enumerate(line):
		c = line[len(line)-i-1]
		if c != ' ':
			c = match[c]
			linetotal *= 5
			linetotal += points[c]
			# print(c, linetotal)
	total.append(linetotal)
total.sort()
# print(len(total), len(total) / 2)
print(total[int(len(total)/2)])
# print(total)
