from util import prob

def rstr(s, gc, n):
    return round(1 - (1 - prob(s, gc))**n, 3)

with open('rstr.in', 'r') as fp:
    lines = [line.rstrip() for line in fp.readlines()]

n, gc = [float(x) for x in lines[0].split(' ')]
s = lines[1]

print rstr(s, gc, n)
