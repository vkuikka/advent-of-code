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

print(len(nums))
for i, num in enumerate(nums):
	if nums[i][0] > folds[0][1]:
		n = nums[i][0]
		f = folds[0][1]
		nums[i][0] = f - (n - f)
remove_duplicates()
print(len(nums))

