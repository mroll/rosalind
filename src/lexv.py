from util import kmers

with open('lexv.in', 'r') as fp:
    lines = [line.rstrip() for line in fp.readlines()]

alphabet = lines[0].split(' ')
n = int(lines[1])

lexcmp = lex_order_fn(alphabet)

strings = kmers(alphabet, sizerange=[1,n+1])
for s in sorted(strings, cmp=lexcmp):
    print s
