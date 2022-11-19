N,Q = map(int,input().split())
A = [int(n) for n in input().split()]

class SegmentTree:
    def __init__(self,seq):
        self.size = len(seq)
        self.tree = [0]*(self.size*2)

        for i in range(self.size,self.size*2):
            self.tree[i] = seq[i-self.size]

        for i in range(self.size-1,0,-1):
            self.tree[i] = self.tree[2*i] ^ self.tree[2*i+1]

    def update(self,i,v):
        i += self.size
        self.tree[i] ^= v
        i >>= 1 
        while i > 0:
            self.tree[i] ^= v
            i >>= 1

    def show(self,l,r):
        l += self.size
        r += self.size
        res = 0
        while l < r:
            if l&1:
                res ^= self.tree[l]
                l += 1
            if r&1:
                res ^= self.tree[r-1]
                r -= 1
            l >>= 1
            r >>= 1
        return res

segtree = SegmentTree(A)

for _ in range(Q):
    t,x,y = map(int,input().split())

    if t == 1:
        segtree.update(x-1,y)

    else:
        print(segtree.show(x-1,y))