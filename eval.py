from util import flines, prob

def ss_prob(n, s, gc):
    P_Sn = prob(s, gc)
    return round(P_Sn*(n-len(s)+1), 3)

def _eval(n, s, A):
    return [ss_prob(n, s, gc) for gc in A]

lines = flines('eval.in')

n = int(lines[0])
S = lines[1]
A = [float(x) for x in lines[2].split(' ')]

print ' '.join(map(str, _eval(n, S, A)))
