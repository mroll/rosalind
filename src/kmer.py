import re
from util import outer_product, parseFasta, fread, occurrences, kmers

fastas = parseFasta(fread('kmer.in'))
S      = fastas[0].seq

A = kmers(['A', 'C', 'T', 'G'], [0, 4])

for x in [occurrences(S, kmer) for kmer in A]:
    print x

# print ' '.join(map(str, [occurrences(S, kmer) for kmer in A]))
