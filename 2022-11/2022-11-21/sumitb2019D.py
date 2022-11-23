import itertools

N = int(input())
S = input()

PIN = itertools.product([str(i) for i in range(10)],repeat=3)

res = 0
for pin in PIN:
    pi = 0
    for i in range(N):
        if S[i] == pin[pi]:
            pi += 1
        if pi == 3:
            res += 1
            break

print(res)
