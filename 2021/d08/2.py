#!/usr/bin/python3
# f = open("input.txt", "r").read().split("\n")
import itertools

def get_num(lets):
	res = -1
	a = lets[0]
	b = lets[1]
	c = lets[2]
	d = lets[3]
	e = lets[4]
	f = lets[5]
	g = lets[6]
	if a and b and c and not d and e and f and g:
		res = 0
	if not a and not b and c and not d and not e and f and not g:
		res = 1
	if a and not b and c and d and e and not f and g:
		res = 2
	if a and not b and c and d and not e and f and g:
		res = 3
	if not a and b and c and d and not e and f and not g:
		res = 4
	if a and b and not c and d and not e and f and g:
		res = 5
	if a and b and not c and d and e and f and g:
		res = 6
	if a and not b and c and not d and not e and f and not g:
		res = 7
	if a and b and c and d and e and f and g:
		res = 8
	if a and b and c and d and not e and f and g:
		res = 9
	return (res)

def get_order():
	lets = "abcdefg"
	for order in itertools.permutations(lets):
		res = -1
		for each in line[0]:
			lets = []
			for i in range(7):
				lets.append(each.count(order[i]))
			res = get_num(lets)
			if res == -1:
				break
		if res != -1:
			return (order)

f = open("input.txt", "r").read().split("\n")

for i, num in enumerate(f):
	f[i] = f[i].split("|")
	f[i][0] = f[i][0].strip()
	f[i][1] = f[i][1].strip()
	f[i][0] = f[i][0].split(" ")
	f[i][1] = f[i][1].split(" ")

total = 0
for line in f:
	pattern = line[0]
	output = line[1]

	# SIGNAL PATTERN
	checks = {}
	order = get_order()
	for each in pattern:
		lets = []
		for i in range(7):
			lets.append(each.count(order[i]))
		res = get_num(lets)
		if res != -1:
			checks[each] = res

	# OUTPUT VALUE
	result = ''
	for each in output:
		tmp = ''
		for c in checks:
			if len(each) != len(c):
				continue
			valid = 1
			for letter in c:
				if letter not in each:
					valid = 0
			if valid:
				tmp += str(checks[c])
		if tmp != '':
			result += str(tmp)

	# TOTAL RESULT
	if result != '':
		total += int(result)
print(total)
