N = int(input())
S = input()
W = [int(n) for n in input().split()]

Correct = [(w,s) for w,s in zip(W,S)]
Correct.sort()

res = S.count('0')
score = res

for i in range(N):
    if Correct[i][1] == '0':
        score -= 1
    else:
        score += 1
    if i+1 < N and Correct[i][0] == Correct[i+1][0]:
        continue
    res = min(res,score)

print(N-res)
