#!/usr/bin/env python3
def check_ans(check, group):
	all_valid = 1
	for ans in group:
		valid = 0
		for c in ans:
			if c == check:
				valid = 1
		if not valid:
			all_valid = 0
	return all_valid

input = open("input.txt", "r").read()
groups = input.split('\n\n')

for i, g in enumerate(groups):
	groups[i] = g.split('\n')
res = 0
for g in groups:
	same_ans = []
	for answers in g:
		for c in answers:
			if not c in same_ans and check_ans(c, g):
				same_ans.append(c)
	res += len(same_ans)
print(res)
