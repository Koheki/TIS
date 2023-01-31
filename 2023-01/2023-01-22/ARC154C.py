T = int(input())

for _ in range(T):
    N = int(input())
    A = set([int(n) for n in input().split()])
    B = set([int(n) for n in input().split()])

    res = "Yes"
    for b in B:
        if b not in A:
            res = "No"
            break
    print(res)
