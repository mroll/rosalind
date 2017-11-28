import util

def nthcol(m, n):
    return map(lambda x: x[n], m)

# requires sorted l
# def freqs(l):
#     res = {}
# 
#     curr_el   = l[0]
#     curr_freq = 0
#     for x in l:
#         if curr_el != x:
#             res[curr_el] = curr_freq
#             curr_el   = x
#             curr_freq = 0
# 
#         curr_freq += 1
# 
#     res[curr_el] = curr_freq
#     return res

def maxidx(l):
    mx  = l[0]
    idx = 0

    for i in range(len(l)):
        if l[i] > mx:
            mx = l[i]
            idx = i

    return idx

def freq(l, x):
    r = 0
    for y in l:
        if y == x:
            r += 1

    return r

def zeros(n):
    return [0] * n

def cols(M):
    return map(lambda i: map(lambda j: M[j][i], range(len(M))), range(len(M[0])))

def cons(fname):
    fs      = util.parseFasta(util.fread(fname))
    M       = map(lambda x: x.seq, fs)
    columns = map(lambda c: map(str, c), cols(M))
    ncols   = len(columns)

    freqs = { c : zeros(ncols) for c in "ACGT" }
    
    for i in range(ncols):
        for c in columns[i]:
            freqs[c][i] += 1

    return freqs

freqs = cons("cons.txt")

L = "ACGT"

vals = [freqs[c] for c in L]

print "".join(map(lambda i: L[i], map(maxidx, cols(vals))))

print "A: {}".format(" ".join(map(str, freqs['A'])))
print "C: {}".format(" ".join(map(str, freqs['C'])))
print "G: {}".format(" ".join(map(str, freqs['G'])))
print "T: {}".format(" ".join(map(str, freqs['T'])))
