class UnionFind:
    def __init__(self):
        n = 10**6
        self.parent = [i for i in range(n)]

    def root(self,i):
        if self.parent[i] != i:
            self.parent[i] = self.root(self.parent[i])
        return self.parent[i]

    def unite(self,x,y):
        

    def show(self,i):
        return self.root(i)

N,Q = map(int,input().split())

unitree = UnionFind(N)

for _ in range(Q):
    op = map(int,input().split())

    if op[0] == 1:


    elif op[0] == 2:

    else:
