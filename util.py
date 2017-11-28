import re
from functools import reduce


class Fasta:
    def __init__(self, hdr, seq):
        self.hdr = hdr
        self.seq = seq

def parseFasta(fs):
    fastas = []

    state = None
    hdr = None
    seq = None

    for ch in fs:
        if ch == ">":
            if hdr != None and seq != None:
                fastas.append(Fasta(hdr, seq))

            state = "hdr"
            hdr = ""
            continue

        if ch == "\n":
            if state == "hdr":
                state = "seq"
                seq = ""
            continue


        if state == "hdr":
            hdr += ch

        if state == "seq":
            seq += ch

    fastas.append(Fasta(hdr, seq))

    return fastas

def fread(fname):
    with open(fname, "r") as fp:
        return fp.read()

def zeros(n):
    return [0] * n


DNACodonTable = { "TTT": "F",      "CTT": "L",      "ATT": "I",      "GTT": "V",
                  "TTC": "F",      "CTC": "L",      "ATC": "I",      "GTC": "V",
                  "TTA": "L",      "CTA": "L",      "ATA": "I",      "GTA": "V",
                  "TTG": "L",      "CTG": "L",      "ATG": "M",      "GTG": "V",
                  "TCT": "S",      "CCT": "P",      "ACT": "T",      "GCT": "A",
                  "TCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
                  "TCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
                  "TCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
                  "TAT": "Y",      "CAT": "H",      "AAT": "N",      "GAT": "D",
                  "TAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
                  "TAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
                  "TAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
                  "TGT": "C",      "CGT": "R",      "AGT": "S",      "GGT": "G",
                  "TGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
                  "TGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
                  "TGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G" }

def reverse_comp(dna_string):
    comp = ""
    for ch in dna_string:
        if ch == "A":
            comp += "T"
        elif ch == "T":
            comp += "A"
        elif ch == "C":
            comp += "G"
        elif ch == "G":
            comp += "C"

    return comp[::-1]

def open_reading_frames(dna_string):
    global DNACodonTable

    n    = len(dna_string)
    orfs = []

    for i in range(n-3):
        if dna_string[i:i+3] == "ATG":
            orf   = "ATG"
            valid = False
            j     = i + 3

            while j <= n-3:
                if DNACodonTable[dna_string[j:j+3]] is "Stop":
                    valid = True
                    orf   += dna_string[j:j+3]

                    break

                orf += dna_string[j:j+3]
                j   += 3

            if valid:
                orfs.append(orf)

    return orfs

def transcribe(codon_string, table):
    return "".join([table[codon_string[i:i+3]] for i in range(0, len(codon_string)-3, 3)])

def even_speedup_perms(A):
    def non_zero_dirs(dirs):
        for v in dirs.values():
            if v is not 0:
                return True

        return False

    A.sort()
    dirs = {x: -1 for x in A}
    dirs[A[0]] = 0

    res = [list(A)]

    while non_zero_dirs(dirs):
        max_non_zero_el = max([el for el in A if dirs[el] is not 0])
        pos_el = A.index(max_non_zero_el)
        adj_el = A.index(max_non_zero_el) + dirs[max_non_zero_el]
        
        A[pos_el], A[adj_el] = A[adj_el], A[pos_el]
        res.append(list(A))

        if adj_el == 0 or adj_el == len(A)-1 or A[adj_el + dirs[max_non_zero_el]] > max_non_zero_el:
            dirs[max_non_zero_el] = 0

        for i in range(adj_el):
            if A[i] > max_non_zero_el:
                dirs[A[i]] = 1

        for i in range(adj_el+1, len(A)):
            if A[i] > max_non_zero_el:
                dirs[A[i]] = -1

    return res

def lex_perms(A):
    """
    Lexicographical ordering of permutations:
        1. Find the index of the start of the longest non-decreasing sequence.
        2. Set pivot = this index - 1.
        3. Find the index j > pivot s.t. A[j] > A[pivot].
        4. Swap A[j], A[pivot].
        5. Reverse A[pivot+1:]
    """

    L = list(A)
    L.sort()

    def find_pivot(L):
        for i in range(len(L)-1, 0, -1):
            if L[i-1] < L[i]:
                return i-1
        return None

    n = len(L)
    res = [list(L)]

    pivot = find_pivot(L)
    while pivot is not None:
        for j in range(n-1, pivot, -1):
            if L[pivot] < L[j]:
                L[pivot], L[j] = L[j], L[pivot]
                break

        L[pivot+1:] = L[pivot+1:][::-1]
        res.append(list(L))

        pivot = find_pivot(L)

    return res

def fact(n, mod=1):
    def w_mod(n, mod):
        return int(reduce(lambda x,y: (x % mod) * y, range(2,n+1)))

    def wout_mod(n):
        res = n
        for i in range(n-1, 0, -1):
            res *= i
        return res

    if mod == 1:
        return wout_mod(n)
    else:
        return w_mod(n, mod)

MonoisotopicMassTable = { "A":   71.03711,
        "C":   103.00919,
        "D":   115.02694,
        "E":   129.04259,
        "F":   147.06841,
        "G":   57.02146 ,
        "H":   137.05891,
        "I":   113.08406,
        "K":   128.09496,
        "L":   113.08406,
        "M":   131.04049,
        "N":   114.04293,
        "P":   97.05276 ,
        "Q":   128.05858,
        "R":   156.10111,
        "S":   87.03203 ,
        "T":   101.04768,
        "V":   99.06841 ,
        "W":   186.07931,
        "Y":   163.06333 }

InverseMonoisotopicMassTable = {round(v, 3): k for k, v in MonoisotopicMassTable.items()}

def outer_product(lists):
    n = len(lists)
    list_lengths = [len(l) for l in lists]
    indices = [0] * n
    res = [[lists[i][indices[i]] for i in range(n)]]

    while True:
        done = True
        for i in range(n-1, -1, -1):
            if indices[i] < list_lengths[i]-1:
                done = False
                indices[i] += 1
                for k in range(i+1, n):
                    indices[k] = 0
                break

        if done: break

        res.append([lists[i][indices[i]] for i in range(n)])

    return res

def perfect_matchings(n):
    """
    Returns the number of perfect matchings for a complete graph
    having 2n nodes.
    """
    return reduce(lambda x,y: x*y, [(2*i - 1) for i in range(1,n+1)])

def ATCG(S):
    return [S.count(ch) for ch in ['A', 'T', 'C', 'G']]

def hamm(s, t):
    return sum([1 for i in range(len(s)) if s[i] != t[i]])

def hamming_errors(s, t):
    return [(s[i], t[i]) for i in range(len(s)) if s[i] != t[i]]

def purine_p(x):
    return x == 'A' or x == 'G'

def pyramidine_p(x):
    return x == 'C' or x == 'T'

def pyramidines_p(xs):
    return reduce(lambda x,y: x and y, map(pyramidine_p, xs))

def purines_p(xs):
    return reduce(lambda x,y: x and y, map(purine_p, xs))

def transition_p(xs):
    return purines_p(xs) or pyramidines_p(xs)

def transversion_p(xs):
    return not transition_p(xs)

def kmers(alphabet, sizerange=[0, 2]):
    """
    Return all possible k-mers of size n over the alphabet
    ordered lexicographically.
    """
    
    start, stop = sizerange

    return sorted(reduce(lambda x,y: x+y, [["".join(x) for x in outer_product([alphabet] * i)] for i in range(start,stop)]))

def occurrences(text, pattern):
    count = start = 0
    while True:
        start = text.find(pattern, start) + 1
        if start > 0:
            count += 1
        else:
            return count

def suffixp(s, t):
    """
    Return whether or not s is a suffix of t
    """

    if len(s) > len(t):
        return False

    n = len(s)
    t_start = len(t) - n

    for i in range(n):
        if s[i] is not t[t_start+i]:
            return False

    return True

def kmp_prefix_fn(P):
    n = len(P) + 1
    pi = [0] * n
    k = 0

    for q in range(2,n):
        while k > 0 and P[k] != P[q-1]:
            k = pi[k]

        if P[k] == P[q-1]:
            k += 1

        pi[q] = k

    return pi[1:]

def bitmasks(n):
    def pad(s, n):
        if len(s) < n:
            s = '0' * (n - len(s)) + s
        return s

    return [pad(bin(i)[2:], n) for i in range(2**n)]

def apply_mask(s, mask):
    return [s[i] for i in range(len(s)) if mask[i] == '1']

def subsets(S, size=-1):
    res = [apply_mask(S, m) for m in bitmasks(len(S))]

    if size != -1:
        return [ss for ss in res if len(ss) == size]
    else:
        return res

def lex_order_fn(alphabet):
    indices = {alphabet[i] : i for i in range(len(alphabet))}

    def lex_cmp(s, t):
        mod = 1
        if len(t) < len(s):
            s, t = t, s
            mod = -1

        for i in range(len(s)):
            if s[i] != t[i]:
                if indices[s[i]] < indices[t[i]]:
                    return -1 * mod
                else:
                    return 1 * mod

        if i == len(s)-1:
            return 0
        else:
            return -1 * mod

    return lex_cmp

def prob(S, gc):
    """
    Return the probability of constructing a random string
    that exactly matches S where GC-content = gc.
    """

    As, Ts, Cs, Gs = ATCG(S)
    P_AT = (1 - gc)/2
    P_GC = gc / 2

    return P_AT**(As + Ts) * P_GC**(Cs + Gs)

def fastas(fname):
    return parseFasta(fread(fname))

def motif_pos(protein, motif):
    pattern = re.compile(motif)

    m = pattern.search(protein)

    res = []

    while m:
        start = m.start()
        res.append(start+1)
        m = pattern.search(protein, start+1)

    return res

def flines(fname):
    with open(fname, 'r') as fp:
        return [line.rstrip() for line in fp.readlines()]

def onefasta(fname):
    return fastas(fname)[0]
