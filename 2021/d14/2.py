#!/usr/bin/python3

def format_template(tmp):
	template = {}
	for i, c in enumerate(tmp):
		if i == len(tmp) - 1:
			break
		pair = tmp[i] + tmp[i + 1]
		if pair not in template:
			template[pair] = 1
		else:
			template[pair] += 1
	return template

def add_new(pair, amount):
	if pair not in new:
		new[pair] = amount
	else:
		new[pair] += amount

f = open("input.txt", "r").read().split("\n")
tmp = f[0]
template = format_template(tmp)
pairs = {}
for i, row in enumerate(f):
	if i > 1:
		tmp = row.split(" -> ")
		pairs[tmp[0]] = tmp[1]

iters = 40
for ite in range(iters):
	print(ite/iters, end="\r")
	new = {}
	for i, temp in enumerate(template):
		p1 = temp[0] + pairs[temp]
		p2 = pairs[temp] + temp[1]
		# print(template)
		if temp in template:
			add_new(p1, template[temp])
		if temp in template:
			add_new(p2, template[temp])
	# 	print(temp, "->", p1, p2, new)
	# print(new)
	template = new.copy()

total = 0
amounts = {}
for c in template:
	if c[0] not in amounts:
		amounts[c[0]] = template[c]
	else:
		amounts[c[0]] += template[c]
	if c[1] not in amounts:
		amounts[c[1]] = template[c]
	else:
		amounts[c[1]] += template[c]
	total += template[c]

# print(amounts)
for c in amounts:
	amounts[c] = amounts[c] // 2 + amounts[c] % 2
# print(amounts)

ma = 0
mi = 0
for each in amounts:
	if amounts[each] > ma:
		ma = amounts[each]
	if amounts[each] < mi or mi == 0:
		mi = amounts[each]
# print()
# print("total length", total + 1)
# print(ma, mi)
# print()
print(int(ma - mi))
