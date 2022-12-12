S = input()
T = input()

res = -1

for i in range(len(S)):
    if S[i] != T[i]:
        res = i+1
        break

if res == -1:
    print(len(T))
else:
    print(res)

