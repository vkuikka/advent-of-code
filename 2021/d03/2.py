#!/usr/bin/python3

def	validate(line, compare, bit):
	for j, _ in enumerate(line):
		if j < bit and compare[j] != line[j]:
			return 0
	return 1

def print_result(e, g):
	e = "".join(e)
	g = "".join(g)
	num1 = 0
	num2 = 0
	for digit in e:
		num1 = num1 * 2 + int(digit)
	for digit in g:
		num2 = num2 * 2 + int(digit)
	print(num1)
	print(num2)
	print(num1 * num2)

f = open("input.txt", "r").read().split("\n")
e = list("000000000000")
g = list("000000000000")
for bit, _ in enumerate(f[0]):
	a1e = 0
	a0e = 0
	a1g = 0
	a0g = 0
	for i, line in enumerate(f):
		if validate(line, e, bit):
			if (line[bit] == '0'):
				a0e += 1
			if (line[bit] == '1'):
				a1e += 1
		if validate(line, g, bit):
			if (line[bit] == '0'):
				a0g += 1
			if (line[bit] == '1'):
				a1g += 1
	if (a0e > a1e):
		e[bit] = '0'
	else:
		e[bit] = '1'

	if (a0g == 0 and a1g > 0):
		g[bit] = '1'
	elif (a1g == 0 and a0g > 0):
		g[bit] = '0'
	else:
		if (a0g > a1g):
			g[bit] = '1'
		else:
			g[bit] = '0'
print_result(e, g)
