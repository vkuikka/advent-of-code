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

f = open('input.txt', 'r').read().split('\n')[0]

# f = '8A004A801A8002F478'
# f = '620080001611562C8802118E34'
# f = 'C0015000016115A2E0802F182340'
# f = 'A0016C880162017C3686B18A3D4780'

# 1 + 2 = 3
# f = 'C200B40A82'

# prod = 54
# f = '04005AC33890'

# min = 7
# f = '880086C3E88112'

# max = 9
# f = 'CE00C43D881120'

# less than = true
# f = 'D8005AC2A8F0'

# greater than = false
# f = 'F600BC2D8F'

# equal to = false
# f = '9C005AC2F8F0'

# true, because 1 + 3 = 2 * 2
# f = '9C0141080250320F1802104A08'

added = 0
depth = 0

hex_bin = {
	'0' : '0000',
	'1' : '0001',
	'2' : '0010',
	'3' : '0011',
	'4' : '0100',
	'5' : '0101',
	'6' : '0110',
	'7' : '0111',
	'8' : '1000',
	'9' : '1001',
	'A' : '1010',
	'B' : '1011',
	'C' : '1100',
	'D' : '1101',
	'E' : '1110',
	'F' : '1111'
}
bin_hex = {}
for key in hex_bin:
	bin_hex[hex_bin[key]] = key

def parse_literal(b):
	global index
	i = index
	msg = []
	while (b[i] == '1'):
		n = b[i+1:i+5]
		i += 5
		msg.append(bin_hex[n])
	n = b[i+1:i+5]
	i += 5
	msg.append(bin_hex[n])
	s = ''
	for each in msg:
		s += each
	index = i
	return (int(s, 16))

asd = 0

def parse_operator(b):
	global index, depth, asd
	length = 0
	sub_packets = 0
	length_type = b[index]
	index += 1
	if length_type == '0':
		length = 15
		sub_length = int(b[index:index+length], 2)
	else:
		length = 11
		sub_packets = int(b[index:index+length], 2)
		sub_length = 0
	index += length
	og = index
	nums = []
	packet = 0
	while index - og < sub_length or packet < sub_packets:
		packet += 1
		tmp = index
		index = 0
		depth += 1
		num = parse_message(b[tmp:], sub_length)
		depth -= 1
		if num == True:
			num = 1
		elif num == False:
			num = 0
		if num != -1:
			nums.append(num)
		index = tmp + index
		# print(bcol.WARNING, depth * '| ' + bcol.OKBLUE + "nums", nums, bcol.ENDC)
	return (nums)

def parse_message(b, paintlen):
	global added, index, depth

	version_bin = b[index:index+3]
	index += 3
	type_ID_bin = b[index:index+3]
	index += 3
	version = int(version_bin, 2)
	type_ID = int(type_ID_bin, 2)
	if index > len(b) - 4:
		return -1
	added += version
	if type_ID == 4:
		num = parse_literal(b)
		# print(bcol.WARNING, depth * '| ' + bcol.OKBLUE + "literal", num, bcol.ENDC)
		return num
	else:
		# print(bcol.WARNING, depth * '| ' + bcol.WARNING + "id", type_ID, "operator", bcol.ENDC)
		num = parse_operator(b)
		# print(bcol.WARNING, depth * '| ' + bcol.OKGREEN + "id", type_ID, "operator", num, bcol.ENDC)
		if type(num) == int:
			return (num)
		res = num[0]
		for i, n in enumerate(num):
			if i != 0:
				if type_ID == 0:
					res += n
				if type_ID == 1:
					res *= n
				if type_ID == 2:
					res = min(res, n)
				if type_ID == 3:
					res = max(res, n)
				if type_ID == 5:
					res = (num[0] > num[1])
				if type_ID == 6:
					res = (num[0] < num[1])
				if type_ID == 7:
					res = (num[0] == num[1])
		return (res)
binary = ''
for i, c in enumerate(f):
	binary += hex_bin[c]
index = 0
num = parse_message(binary, 0)

print("part 1:",added)
print("part 2:", num)
