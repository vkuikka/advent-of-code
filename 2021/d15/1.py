#!/usr/bin/python3
class bcol:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

mindist = 0

def gonext(x, y, dist, visited):
	global mindist

	# optimization to skip left bot and right top corners
	if abs(x - y) > 50:
		return

	if x >= len(f[0]) or y >= len(f) or x < 0 or y < 0:
		return
	if (x, y) in visited:
		return
	dist += tmp[y][x]['num']
	if dist >= tmp[y][x]['min'] and tmp[y][x]['min'] != -1:
		return
	if dist < tmp[y][x]['min'] or tmp[y][x]['min'] == -1:
		tmp[y][x]['min'] = dist
	if dist >= mindist:
		return

	if x == len(f[0]) - 1 and y == len(f) - 1:
		if dist < mindist:
			mindist = dist
			# debigging live view of explored map area
			m = ''
			for a in tmp:
				for n in a:
					if n['min'] == -1:
						m += bcol.FAIL + '. '
					else:
						m += bcol.OKGREEN + '0 '
				m += '\n'
			print(m)
			print(mindist)
		return

	visited.append((x, y))
	gonext(x + 1, y, dist, visited.copy())
	gonext(x, y + 1, dist, visited.copy())
	gonext(x - 1, y, dist, visited.copy())
	gonext(x, y - 1, dist, visited.copy())


f = open("input.txt", "r").read().split("\n")
# f = ["122", "212", "221"]

tmp = []
for y, row in enumerate(f):
	tmp.append([])
	for x, col in enumerate(row):
		t = {}
		t['num'] = int(f[y][x])
		t['min'] = -1
		tmp[y].append(t)


# init smallest distance
for i in range(len(tmp)):
	mindist += tmp[i][0]['num']
for i in range(len(tmp[0])):
	mindist += tmp[len(tmp) - 1][i]['num']

# search
gonext(0, 0, 0, [])


for y in range(len(tmp)):
	for x in range(len(tmp[0])):
		print(tmp[y][x]['min'], end=',')
	print()
print()


# top left corner
for x in range(4):
	for y in range(4):
		print(tmp[y][x]['min'], end=" ")
	print()
print()
# bot right corner
for x in range(1,5):
	for y in range(1,5):
		print(tmp[len(f) - y][len(f[0]) - x]['min'], end=" ")
	print()
print()

print("result: ", tmp[len(f) - 1][len(f[0]) - 1]['min'] - tmp[0][0]['min'])
