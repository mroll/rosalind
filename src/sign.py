from util import outer_product, lex_perms

def sign(n):
    res = []
    lists = [[i, -i] for i in range(1, n+1)]

    for combo in outer_product(lists):
        for perm in lex_perms(combo):
            res.append(perm)

    return res

ps = sign(5)

print len(ps)
for p in ps:
    print " ".join(map(str, p))
