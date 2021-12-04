#!/usr/bin/python3

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
	g_count = 0
	e_count = 0
	for i, line in enumerate(f):
		if line[bit] == '1':
			e_count += 1
		else:
			g_count += 1
	if (e_count > g_count):
		e[bit] = '0'
	else:
		e[bit] = '1'
	if (e_count > g_count):
		g[bit] = '1'
	else:
		g[bit] = '0'
print_result(e, g)
