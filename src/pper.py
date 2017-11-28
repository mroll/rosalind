from util import fact, flines
from functools import reduce

def n_partial_perms(n, k, mod=1):
    return int(reduce(lambda x,y: (x % mod) * y, range(n-k+1, n+1)) % mod)

# what this looks like in prefix notation
# ---------------------------------------
# (int (% (reduce (lambda (x y)
#                   (* (% x mod) y))
#                 (range (1+ (- n k))
#                        (1+ n))))

n, k = map(int, flines('pper.in')[0].split(' '))

print(n_partial_perms(n, k, mod=1e6))
