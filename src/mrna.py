from util import DNACodonTable, flines
from functools import reduce

def mrna(s):
    """
    Returns the number of ways protein string s could have been
    translated.
    """

    vals  = list(DNACodonTable.values())
    
    return int(reduce(lambda x,y: (x % 1e6) * y, [vals.count(ch) for ch in s] + [vals.count('Stop')]))

data = flines('mrna.in')

print(mrna(data[0]))
