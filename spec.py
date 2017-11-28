from util import flines, MonoisotopicMassTable

def spec(L):
    def aa_from_weight(w):
        for k,v in MonoisotopicMassTable.items():
            if abs(v - w) < tol:
                return k

        return None

    tol = 0.005

    return ''.join([aa_from_weight(w) for w in [round(L[i+1] - L[i], 3) for i in range(len(L)-1)]])


L = map(float, flines('spec.in'))

print spec(L)
