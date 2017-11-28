class SuffixNode:
    def __init__(self, link = None):
        self.children = {}
        if link is not None:
            self.link = link
        else:
            self.link = self

    def add_child(self, c, v):
        self.children[c] = v

    def add_link(self, link):
        self.link = link

def Algorithm1(T):
    root = SuffixNode()
    top  = SuffixNode(link = root)
    root.add_child(T[0], top)

    for c in T[1:]:
        r = top
        oldrp = None
        while c not in r.children:
            rp = SuffixNode()
            r.add_child(c, rp)

            if oldrp is not None:
                oldrp.add_link(rp)

            oldrp = rp
            r = r.link

        if r is root:
            oldrp.add_link(root)
        else:
            oldrp.add_link(r.children[c])
        top = top.children[c]

    return root

T = "cacao"
root = Algorithm1(T)
print root.children

def test_and_split(s, ref, t):
    k, p = ref
    if k <= p:
        sp = s.children[T[k]]
        if t == 

def update(root, T, s, ref):
    oldr = root
    branch = test_and_split(s, ref, t)


