N = int(input())

res = []
for _ in range(N):
    res.append(input())

res.reverse()
for i in range(N):
    print(res[i])
