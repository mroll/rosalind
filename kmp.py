from util import parseFasta, fread, kmp_prefix_fn

fastas = parseFasta(fread('kmp.in'))

s = fastas[0].seq

print " ".join(map(str, kmp_prefix_fn(s)))
