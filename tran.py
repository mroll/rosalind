from util import parseFasta, fread, transition_p, hamming_errors

def tran(s, t):
    n      = len(s)
    errs   = hamming_errors(s, t)
    ntrans = sum([1 for i in range(len(errs)) if transition_p(errs[i])])

    return float(ntrans) / (len(errs) - ntrans)

fastas = parseFasta(fread("tran.in"))

s = fastas[0].seq
t = fastas[1].seq

print tran(s, t)
