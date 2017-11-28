from util import outer_product

with open('lexf.in', 'r') as fp:
    lines = [line.rstrip() for line in fp.readlines()]

alphabet = lines[0].split(' ')
n = int(lines[1])

strings = ["".join(x) for x in outer_product([alphabet] * n)]

strings.sort()
for x in strings:
    print x
