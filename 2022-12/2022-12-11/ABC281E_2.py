import heapq

class Double_Heap:
    def __init__(self):
        self.__small = []
        self.__large = []
        self.__dict = {}
        self.__length = 0
        self.__sum = 0

    def __bool__(self):
        return bool(self.__length)
    
    def __len__(self):
        return self.__length

    def __contains__(self,x):
        return self.is_exit(x)
    
    def push(self,x):
        self.__length += 1
        self.__sum += x
    
        heapq.heappush(self.__small,x)
        heapq.heappush(self.__large,-x)

        if x in self.__dict:
            self.__dict[x] += 1
        else:
            self.__dict[x] = 1

    def discord(self,x):
        if x not in self:
            return 

        self.__dict[x] -= 1
        if self.__dict[x] == 0:
            del self.__dict[x]

        self.__length -= 1
        self.__sum -= x

        while self.__small and (self.__small[0] not in self):
            heapq.heappop(self.__small)

        while self.__large and (-self.__large[0] not in self):
            heapq.heappop(self.__large)

    def is_exit(self,x):
        return x in self.__dict

    def get_min(self):
        assert self
        return self.__small[0]

    def pop_min(self):
        assert self
        x = self.get_min()
        self.discord(x)
        return x
    
    def get_max(self):
        assert self
        return -self.__large[0]

    def pop_max(self):
        assert self
        x = self.get_max()
        self.discord(x)
        return x

    def count(self,x):
        return self.__dict.get(x,0)

    def sum(self):
        return self.__sum


N,M,K = map(int,input().split())
A = [int(n) for n in input().split()]

L,R = Double_Heap(),Double_Heap()

for i, a in enumerate(sorted(A[:M])):
    if i < K:
        L.push(a)
    else:
        R.push(a)

res = [0]*(N-M+1)
res[0] = L.sum()

for i in range(N-M):

    if A[i+M] <= L.get_max():
        L.push(A[i+M])
    else:
        R.push(A[i+M])
    
    if A[i] in L:
        L.discord(A[i])
    else:
        R.discord(A[i])

    if len(L) > K:
        R.push(L.pop_max())
    elif len(L) < K:
        L.push(R.pop_min())
    
    res[i+1] = L.sum()

print(*res)
