#!/usr/bin/python3
def gonext(i, j):
	if i < 0 or j < 0 or i >= len(f) or j >= len(line):
		return 0
	top = f[i-1][j][0] if i > 0 else -1
	left = f[i][j-1][0] if j > 0 else -1
	right = f[i][j+1][0] if j < len(line)-1 else -1
	bot = f[i+1][j][0] if i < len(f)-1 else -1
	total = 0
	if left > f[i][j][0] and left < 9:
		total += gonext(i, j-1)
	if right > f[i][j][0] and right < 9:
		total += gonext(i, j+1)
	if top > f[i][j][0] and top < 9:
		total += gonext(i-1, j)
	if bot > f[i][j][0] and bot < 9:
		total += gonext(i+1, j)
	if f[i][j][1] == 0:
		f[i][j][1] = 1
		return (1 + total)
	f[i][j][1] = 1
	return (0)

f = open("input.txt", "r").read().split("\n")
for i, row in enumerate(f):
	f[i] = list(row)
	for j, num in enumerate(row):
		f[i][j] = [int(num), 0]
top1 = 0
top2 = 0
top3 = 0
for i, line in enumerate(f):
	for j, num in enumerate(line):
		if num[1] == 0:
			total = gonext(i, j)
			if total > top1:
				top3 = top2
				top2 = top1
				top1 = total
			elif total > top2:
				top3 = top2
				top2 = total
			elif total > top3:
				top3 = total
			for k, row in enumerate(f):
				for l, num in enumerate(row):
					if num[1] != 0:
						f[k][l][1] = 0
print(top1)
print(top2)
print(top3)
print(top1 * top2 * top3)
