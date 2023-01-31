class SegmentTree:
    def __init__(self,n):
        self.n = n
        self.size = 1 << (n-1).bit_length()
        self.tree = [0]*2*self.size
    
    def update(self,i,v):
        i += self.size
        self.tree[i] += v
        while i > 1:
            self.tree[i>>1] = self.tree[i]+self.tree[i^1]
            i >>= 1

    def query(self,l,r):
        res = 0
        l += self.size
        r += self.size

        while l < r:
            if l&1:
                res += self.tree[l]
                l += 1
            if r&1:
                res += self.tree[r-1]
                r -= 1
            l >>= 1
            r >>= 1
        return res

N = int(input())
S = [s for s in input()]
Q = int(input())

is_sorted = SegmentTree(N)
counts = [SegmentTree(N) for _ in range(26)]

for i in range(N):
    s = S[i]
    counts[ord(s)-ord('a')].update(i,1)

for i in range(N-1):
    if S[i] > S[i+1]:
        is_sorted.update(i,1)

for _ in range(Q):
    query = [q for q in input().split()]

    if query[0] == '1':
        x = int(query[1])-1
        p = ord(S[x]) - ord('a')
        c = ord(query[2]) - ord('a')
        counts[p].update(x,-1)
        if 1 <= x and S[x-1] > S[x]:
            is_sorted.update(x-1,-1)
        if x+1 < N and S[x] > S[x+1]:
            is_sorted.update(x,-1)

        S[i] = query[2]
        counts[c].update(x,1)
        if 1 <= x and S[x-1] > S[x]:
            is_sorted.update(x-1,-1)
        if x+1 < N and S[x] > S[x+1]:
            is_sorted.update(x,-1) 

    else:
        l,r = int(query[1])-1, int(query[2])-1
        flag = True
        if is_sorted.query(l+1,r) != 0:
            flag = False
        for s in S[l+1:r]:
            if counts[ord(s)-ord('a')].query(l,r)
