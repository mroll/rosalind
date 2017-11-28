import math
from util import parseFasta, fread, fact

def pmch(S):
    As = S.count("A")
    Cs = S.count("C")

    return fact(As) * fact(Cs)

fastas = parseFasta(fread("pmch.in"))
S = fastas[0].seq

print pmch(S)
