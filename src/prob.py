from math import log

with open("prob.in", "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

s = lines[0]
A = map(float, lines[1].split(' '))

print " ".join(map(str, map(lambda gc: round(log(prob(s, gc), 10), 3), A)))
