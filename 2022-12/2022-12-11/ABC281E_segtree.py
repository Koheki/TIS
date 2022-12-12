class SegmentTree:
    def __init__(self,seq) -> None:
        n = len(seq)
        self.size = 1 << (n-1).bit_length()
        self.tree = [0]*2*self.size

        for i in range(n):
            self.tree[self.size+i] = seq[i]

        for i in range(self.size-1,0,-1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def add(self,i,v):
        i += self.size
        self.tree[i] = v
        while i > 0:
            self.tree[i>>1] = self.tree[i] + self.tree[i^i]
            i >>= 1

    def lower_bound(self,x):