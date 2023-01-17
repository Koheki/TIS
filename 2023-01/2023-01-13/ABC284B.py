T = int(input())

for _ in range(T):
    N = int(input())
    A = [int(n) for n in input().split()]
    res = 0

    for a in A:
        if a%2 == 1:
            res += 1
    print(res)
