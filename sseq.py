from util import parseFasta, fread

def sseq(s, t):
    """
    Return a collection of indices into s where symbols of
    t appear as a subsequence.
    """
    res = []

    curr_t = 0
    for i in range(len(s)):
        if s[i] == t[curr_t]:
            res.append(i+1)
            curr_t += 1

        if curr_t == len(t):
            break

    return res

fastas = parseFasta(fread("sseq.in"))

s = fastas[0].seq
t = fastas[1].seq

print " ".join(map(str, sseq(s, t)))
