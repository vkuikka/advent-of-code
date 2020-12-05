#!/usr/bin/env python3
import sys
def getnum(input_str):
	num = ''
	i = 0
	for c in input_str:
		if c.isdigit():
			num += c
	return int(num)

def check_hcl(str):
	if str[0] != '#' or len(str) != 7:
		return False
	for i, c in enumerate(str):
		if c.isdigit() == False and c.isalpha() == False and i != 0:
			return False
	return True
def check_ecl(str):
	return(
		str == 'amb' or
		str == 'blu' or
		str == 'brn' or
		str == 'gry' or
		str == 'grn' or
		str == 'hzl' or
		str == 'oth')

input = open("input.txt", "r").read()
splitted = input.split('\n\n')

required_fields = "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"

passports = []
for passp, data in enumerate(splitted):
	data = data.split('\n')
	passports.append({})
	for line in data:
		line = line.split(' ')
		for values in line:
			values = values.split(':')
			passports[passp][values[0]] = values[1]

count = 0
for passp in passports:
	valid = 0
	try:
		if ((int(passp["byr"]) >= 1920 and int(passp["byr"]) <= 2002) and 
			(int(passp["iyr"]) >= 2010 and int(passp["iyr"]) <= 2020) and
			(int(passp["eyr"]) >= 2020 and int(passp["eyr"]) <= 2030) and
			((passp["hgt"].find("cm") > 0 and getnum(passp["hgt"]) >= 150 and getnum(passp["hgt"]) <= 193) or
			(passp["hgt"].find("in") > 0 and getnum(passp["hgt"]) >= 59 and getnum(passp["hgt"]) <= 76)) and
			check_hcl(passp["hcl"]) and
			check_ecl(passp["ecl"]) and
			len(str(passp["pid"])) == 9 and
			passp["pid"].isdigit()):
			valid = 1
	except:
		pass
	if valid:
		count += 1

print(count)
