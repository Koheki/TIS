class UnionFind:
    def __init__(self,N,Q):
        self.parent = [ i if i <= N else 0  for i in range(N+Q+1)]
        self.k = N

    def root(self,X):
        if X != self.parent[X]:
            self.parent[X] = self.root(self.parent[X])
        return self.parent[X]

    def unite(self,X,Y):
        x = self.root(X)
        y = self.root(Y)

        self.parent[y] = x


    def add(self,X):
        self.k += 1
        self.parent[self.k] = X

    def find(self,X):
        return self.parent(X)

    def show(self):
        print(self.parent)


N,Q = map(int,input().split())
untree = UnionFind(N,Q)

for _ in range(Q):
    op = [int(n) for n in input().split()]

    if op[0] == 1:
        untree.unite(op[1],op[2])

    elif op[0] == 2:
        untree.add(op[1])

    else:
        print(untree.find(op[1]))
    
    untree.show()