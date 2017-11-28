from util import onefasta

def catalan(n):
    C = [0 for i in range(n+1)]
    C[0] = 1

    for i in range(1, n+1):
        C[i] = sum([C[k-1] * C[i-k] for k in range(1, i+1)])

    return C[n]

def cat(S):
    As = S.count('A')
    Gs = S.count('G')

    return int( ((catalan(As) % 1e6) * (catalan(Gs) % 1e6)) % 1e6)

data = onefasta('cat.in')
print(data.seq)
print(cat(data.seq))
