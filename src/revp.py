from util import parseFasta, fread, reverse_comp

def reverse_pal(S):
    return S == reverse_comp(S)

def revp(S):
    n      = len(S)
    minlen = 4
    maxlen = 12

    res = []
    for length in range(minlen, maxlen+1):
        for start in range(n-length+1):
            if reverse_pal(S[start:start+length]):
                res.append([start+1, length])

    return res

S = parseFasta(fread("revp.in"))[0].seq

for x in revp(S):
    print " ".join(map(str, x))
