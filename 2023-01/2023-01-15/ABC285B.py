N = int(input())
S = input()

for i in range(1,N):
    l = 0
    k = 0
    while k+i < N:
        if S[k] == S[k+i]:
            break
        l += 1
        k += 1
    print(l)
