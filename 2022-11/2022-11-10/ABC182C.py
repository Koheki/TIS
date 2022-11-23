N = input()
k = len(N)
res = 20

for i in range((1<<k)-1,0,-1):
    n = 0
    for j in range(k):
        if (i>>j)&1:
            n += int(N[j])
    if n % 3 == 0:
        res = min(k - bin(i).count("1"),res)
       
if res >= 20:
    print(-1)
else:
    print(res)


# def rec(n,k):
#     res = 0
#     if k == 0:
#         return -1
#     elif int(n)%3 == 0:
#         return 1
#     else:
#         for i in range(k):
#             res += rec(,k-1)