from math import floor

def flines(fname, sep='\n'):
    with open(fname, 'r') as fp:
        return fp.read().strip().split(sep)

def binsearch(A, x):
    n = len(A)

    start = 0
    end   = n-1

    old_mid = -1

    while True:
        mid = start + floor((end-start)/2)

        if mid == old_mid:
            break

        old_mid = mid

        if A[mid] == x:
            return mid+1

        if A[mid] < x:
            start = mid+1
        else:
            end = mid

    return -1

n, m, A, B = flines('bins.in')

A = list(map(int, A.split(' ')))
B = list(map(int, B.split(' ')))

res = [binsearch(A, x) for x in B]

print(' '.join([str(x) for x in res]))
