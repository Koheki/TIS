
class UnionFind:
    def __init__(self,n) -> None:
        self.n = n
        self.parent = [ i for i in range(n)]
        self.siz = [ 1 for _ in range(n)]

    def root(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def unite(self,x,y):
        rootx = self.root(x)
        rooty = self.root(y)

        if rootx != rooty:
            if self.siz[rootx] < self.siz[rooty]:
                self.parent[rootx] = rooty
                self.siz[rooty] += self.siz[rootx]
            else:
                self.parent[rooty] = rootx
                self.siz[rootx] += self.siz[rooty]

    def size(self,x):
        return self.siz[self.root(x)]


N,M = map(int,input().split())

uftree = UnionFind(N)

for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    uftree.unite(a,b)

res = 0
for i in range(N):
    s = uftree.size(i)
    res = max(res,s)

print(res)
