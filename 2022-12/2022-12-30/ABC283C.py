S = input()
res = 0

i,n = 0,len(S)

while i < n:
    if S[i] == '0':
        if i+1 < n and S[i+1] == '0':
            res += 1
            i+=2
            continue
    res += 1
    i+=1

print(res)