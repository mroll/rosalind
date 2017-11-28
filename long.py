from util import *

def overlap(t, s, n=-1):
    tlen, slen = len(t), len(s)
    if slen > tlen:
        return False

    wsize = slen // 2
    tmid, smid = tlen//2, slen//2

    print "Testing ", t, " ", s
    for i in range(1, wsize):
        print t[tlen-wsize-i:], s[:-i]
        print t[:-i], s[i:]
        print
        if t[tlen-wsize+i:] == s[:-i]:
            return t[:-1-i] + s[i:]

        if t[:-i] == s[i:]:
            return s[:-1-i] + t[i:]

    return False
    
def empty(l):
    return len(l) == 0

def debruijn(seq, k):
    n = len(seq)
    kmers = [seq[i:i+k] for i in range(n-k+1)]

    graph = {}
    for kmer in kmers:
        graph[kmer] = []
        for other in kmers:
            if kmer is other: continue

            if kmer[1:] == other[:-1]:
                graph[kmer].append(other)

    return graph

def eulerian_path(g):
    visited = {}

    for k in g.keys():
        if k in visited:
            continue
        
        visited[k] = True
        
        
    

print debruijn("ATGGAAGTCGCGGAATC", 7)


"""
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
"""
