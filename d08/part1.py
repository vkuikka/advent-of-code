#!/usr/bin/env python3
input = open("input.txt", "r").read()
text = input.split('\n')
acc = 0
i = 0
checked = {}
while i < len(text):
	line = text[i].split(' ')
	if i in checked:
		break
	checked[i] = 0
	if line[0] == "acc":
		acc += int(line[1])
	if line[0] == "jmp":
		i += int(line[1])
	else:
		i += 1
print(acc)
