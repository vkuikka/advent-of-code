#!/usr/bin/python3
def remove_duplicates():
	for i, num1 in enumerate(nums):
		for j, num2 in enumerate(nums):
			if num1[0] == num2[0] and num1[1] == num2[1] and i != j:
				nums.pop(i)
				remove_duplicates()
				return

f = open("input.txt", "r").read().split("\n")
nums = []
folds = []
for i, row in enumerate(f):
	if i < 999:
		nums.append(row.split(","))
		nums[i][0] = int(nums[i][0])
		nums[i][1] = int(nums[i][1])
	elif i > 999:
		folds.append(row.split("="))
		folds[i-1000][1] = int(folds[i-1000][1])

for j, fold in enumerate(folds):
	print(" ", j, "/", len(folds), end='\r')
	for i, num in enumerate(nums):
		f = fold[1]
		if fold[0] == 'x':
			n = num[0]
			if n > f:
				nums[i][0] = f - (n - f)
		else:
			n = num[1]
			if n > f:
				nums[i][1] = f - (n - f)
	remove_duplicates()
max_x = 0
max_y = 0
for n in nums:
	max_x = max(max_x, n[0])
	max_y = max(max_y, n[1])
rows, cols = max_x + 1, max_y + 1
arr = [[0] * cols for _ in range(rows)]
for i, n in enumerate(nums):
	arr[n[0]][n[1]] = 1

for x in range(cols):
	for y in range(rows):
		if arr[y][x] == 1:
			print("0", end=" ")
		else:
			print(" ", end=" ")
	print()
