#!/usr/bin/env python3
input = open("input.txt", "r").read()
input = input.split('\n')
for num1 in input:
    n1 = int(num1)
    for num2 in input:
        n2 = int(num2)
        if n1 + n2 == 2020:
            print(n1 * n2)
            exit()
