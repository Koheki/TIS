N = int(input())
S = [s for s in input()]
q = False

for i in range(N):
    if S[i] == '"':
        q = False if q else True

    if S[i] == ',' and q == False:
        S[i] = '.'

print(''.join(S))
