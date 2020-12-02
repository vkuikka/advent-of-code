input = open("input.txt", "r").read()
input = input.split('\n')
for num1 in input:
    n1 = int(num1)
    for num2 in input:
        n2 = int(num2)
        for num3 in input:
            n3 = int(num3)
            if n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
                exit()
