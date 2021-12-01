#!/usr/bin/env python3
input = open("input.txt", "r").read()
groups = input.split('\n\n')
for i, g in enumerate(groups):
	groups[i] = g.split('\n')
res = 0
for g in groups:
	diff_ans = []
	for answers in g:
		for c in answers:
			if not c in diff_ans:
				diff_ans.append(c)
	res += len(diff_ans)
print(res)
