class LazySegTree_RUQ:
    def __init__(self,h,w):
        self.H = 1 << (h-1).bit_length()
        self.W = 1 << (w-1).bit_length()

        self.treeY = [0]*2*self.H
        self.lazyY = [0]*2*self.H
        self.treeX = [0]*2*self.W
        self.lazyX = [0]*2*self.W

        for i in range(h):
            self.treeY[self.H+i] = i
        for j in range(w):
            self.treeX[self.W+j] = j



H,W = map(int,input().split())
A = [[s for s in input()] for _ in range(H)]
pos = [[[h,w] for w in range(W)] for h in range(H)]

Q = int(input())
ab = [[int(n) for n in input().split()] for _ in range(Q)]

