from util import *

seqs = map(lambda x: x.seq, parseFasta(fread("grph.txt")))

def pref(string, n):
    return string[:n]

def suff(string, n):
    return string[-n:]

def overlapp(fs1, fs2, n):
    return suff(fs1, n) == pref(fs2, n)

n = 3

def grph(fname):
    seqs  = parseFasta(fread(fname))
    edges = []

    for x in seqs:
        for y in seqs:
            if x == y: continue

            if overlapp(x.seq, y.seq, n):
                edges.append((x.hdr, y.hdr))

    return edges

for x in grph("grph.txt"):
    print "{} {}".format(x[0], x[1])
