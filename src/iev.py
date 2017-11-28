AAAA = 1 * 2
AAAa = 1 * 2
AAaa = 1 * 2
AaAa = .75 * 2
Aaaa = .5 * 2
aaaa = 0 * 2

probs = [AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa]

with open("iev.txt", "r") as fp:
    couples = fp.read().split()


print sum([float(couples[i]) * probs[i] for i in range(6)])
