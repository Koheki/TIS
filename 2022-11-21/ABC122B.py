S = input()

res = 0
ATGC = {'A','T','G','C'}
tmp = 0

for i in range(len(S)):
    if S[i] not in ATGC:
        res = max(res,tmp)
        tmp = 0
        continue
    tmp += 1

print(max(res,tmp))
