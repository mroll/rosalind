from util import *

def fibd(n, m):
    a   = 1
    b   = 0
    die = 0

    prev = zeros(m-1) + [1]

    for i in range(n):
        die  = prev[0]
        prev = prev[1:] + [a]

        tmp = b
        b = a
        a = a + tmp - die

    return b

def main():
    with open("fibd.txt", "r") as fp:
        n, m = map(int, fp.read().split(" "))

    print fibd(n, m)


main()
