N,M = map(int,input().split())

S = [input() for _ in range(N)]
res = 0

for i in range(N):
    for j in range(i+1,N):
        flag = True
        for k in range(M):
            if S[i][k] == 'x' and  S[j][k] == 'x':
                flag = False
                break
        if flag:
            res += 1

print(res)    
