from util import perms, fact

n = 6
print fact(n)

for x in perms(range(1,n+1)):
    print " ".join(map(str, x))
